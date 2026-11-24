# Chatbot de atendimento com IA - Barbearia Corte Fino (negócio fictício)
# Projeto de portfólio do Luciano
#
# Como usar:
#   1. pip install google-genai
#   2. Defina a variável de ambiente GEMINI_API_KEY com sua chave
#      (ou cole a chave quando o programa pedir)
#   3. python chatbot.py

import os
from google import genai
from google.genai import types

# Modelo da IA. Se der erro de "model not found", troque pelo nome de um
# modelo listado em https://ai.google.dev/gemini-api/docs/models
MODELO = "gemini-3.5-flash"

# ------------------------------------------------------------------
# INFORMAÇÕES DO NEGÓCIO
# Para usar com outro cliente, é só trocar este texto.
# ------------------------------------------------------------------
INFO_NEGOCIO = """
Nome: Barbearia Corte Fino
Endereço: Rua das Palmeiras, 120 - Centro
Horário: terça a sexta das 9h às 20h, sábado das 8h às 17h. Fechado domingo e segunda.

Serviços e preços:
- Corte masculino: R$ 40 (30 minutos)
- Barba: R$ 30 (20 minutos)
- Corte + barba: R$ 60 (50 minutos)
- Sobrancelha: R$ 15
- Pigmentação de barba: R$ 35

Formas de pagamento: Pix, dinheiro, débito e crédito (até 2x sem juros acima de R$ 100).
Estacionamento: não temos, mas há vagas na rua.
Agendamento: pelo próprio WhatsApp. Atendemos também por ordem de chegada quando há horário livre.
Cancelamento: pode cancelar ou remarcar até 2 horas antes, pelo WhatsApp, sem custo.
"""

INSTRUCOES = f"""
Você é a atendente virtual da Barbearia Corte Fino e conversa com clientes pelo WhatsApp.

Regras:
- Responda em português, de forma simpática, natural e curta (como uma mensagem de WhatsApp).
- Use a formatação do WhatsApp: negrito com UM asterisco (*assim*), nunca com dois.
  Não use títulos (#) nem outra formatação de Markdown.
- Use SOMENTE as informações abaixo. Se não souber a resposta, diga que vai
  chamar um atendente humano e não invente nada.
- Se o cliente quiser agendar, pergunte o serviço, o dia e o horário preferidos,
  e diga que um atendente vai confirmar a disponibilidade.
- Você NÃO tem acesso à agenda. Nunca diga que você mesma vai verificar,
  conferir ou reservar um horário: quem confirma é sempre um atendente.
- Se o cliente pedir para falar com uma pessoa, diga que vai transferir para um atendente.

Informações do negócio:
{INFO_NEGOCIO}
"""


def main():
    chave = os.environ.get("GEMINI_API_KEY") or input("Cole sua chave da API do Gemini: ").strip()
    cliente = genai.Client(api_key=chave)

    conversa = cliente.chats.create(
        model=MODELO,
        config=types.GenerateContentConfig(system_instruction=INSTRUCOES),
    )

    print("\n=== Barbearia Corte Fino - Atendimento Virtual ===")
    print("(digite 'sair' para encerrar)\n")

    while True:
        mensagem = input("Você: ").strip()
        if not mensagem:
            continue
        if mensagem.lower() == "sair":
            print("Até mais!")
            break
        try:
            resposta = conversa.send_message(mensagem)
            # Garantia extra: converte negrito do Markdown (**x**) para o do WhatsApp (*x*)
            texto = resposta.text.replace("**", "*")
            print(f"Barbearia: {texto}\n")
        except Exception as erro:
            print(f"[Erro ao falar com a IA: {erro}]\n")


if __name__ == "__main__":
    main()
