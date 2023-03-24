from slack import WebClient
from coinbot import CoinBot
import os

#Cria o slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

#Jogar a moeda
coin_bot = CoinBot("#bot")

#enviar a mensagem
message = coin_bot.cria_mensagem()

#posta no slack
slack_web_client.chat_postMessage(**message)