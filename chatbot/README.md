# 💈 Chatbot de Atendimento com IA para WhatsApp

Atendente virtual que responde clientes de um pequeno negócio 24 horas por dia: preços, horários, formas de pagamento, agendamento e cancelamento. Feito em Python com a API do Google Gemini.

> **Demonstração:** a *Barbearia Corte Fino* é um negócio **fictício**, criado só para mostrar o projeto.

---

## O problema

Pequenos negócios, como barbearias, salões e clínicas, recebem as mesmas perguntas o dia inteiro pelo WhatsApp: *"quanto custa?"*, *"abre domingo?"*, *"tem horário sábado?"*. Quando a resposta demora, o cliente vai para o concorrente.

## A solução

Um chatbot que:

- ✅ **Responde na hora** perguntas sobre preços, horários, pagamento e localização
- ✅ **Não inventa nada:** se não souber, chama um atendente humano
- ✅ **Encaminha agendamentos:** coleta serviço, dia e horário, e um atendente confirma
- ✅ **Fala como gente:** respostas curtas e simpáticas, no estilo do WhatsApp
- ✅ **Já usa a formatação do WhatsApp** (*negrito* com um asterisco)

## Exemplo de conversa

```
Você: quanto custa corte e barba?
Barbearia: O nosso combo de *Corte + barba* custa *R$ 60* (leva cerca de 50 minutos). 😊
Se quiser agendar, é só me dizer qual o dia e horário da sua preferência que um
atendente vai confirmar a disponibilidade para você!

Você: dá pra parcelar?
Barbearia: Sim, aceitamos pagamento no crédito parcelado em até 2x sem juros para
valores acima de R$ 100. Também aceitamos Pix, dinheiro e débito!

Você: vocês fazem luzes?
Barbearia: Não tenho essa informação sobre luzes no momento. Vou chamar um
*atendente humano* para te ajudar com isso, só um instante! 😊
```

Repare na última resposta: o serviço não está na lista, então o bot **não inventa um preço**. Ele passa a conversa para uma pessoa.

<!-- Coloque aqui os prints ou o GIF da conversa:
![Conversa com o chatbot](prints/conversa.png)
-->

## Funciona para qualquer negócio

Todas as informações ficam em um único bloco de texto (`INFO_NEGOCIO`) no início do `chatbot.py`. Para atender outro cliente, é só trocar esse texto: serviços, preços, horários, endereço e regras. O código não muda.

## Como rodar

**Requisitos:** Python 3.10 ou mais novo e uma chave gratuita da API do Gemini ([Google AI Studio](https://aistudio.google.com/apikey)).

```bash
cd chatbot
pip install google-genai
python chatbot.py
```

O programa pede a chave ao iniciar. Para não precisar colar a chave toda vez, salve-a na variável de ambiente `GEMINI_API_KEY`:

```bash
# Windows
setx GEMINI_API_KEY "sua-chave"
```

Digite `sair` para encerrar.

## Tecnologias

- **Python**
- **Google Gemini API** (`google-genai`)
- **Engenharia de prompt:** instruções de sistema que limitam o bot às informações do negócio

## Próximos passos

- [ ] Integração com o WhatsApp (API oficial do WhatsApp Business ou Z-API)
- [ ] Salvar pedidos de agendamento em uma planilha
- [ ] Avisar o atendente quando o bot transferir a conversa

---

Projeto de portfólio desenvolvido por **Luciano**.
