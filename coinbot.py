#importa a biblioteca para gerar números aleatórios.
import random

class CoinBot: 
    #constante com texto padrão
    COIN_BLOCK = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": (
                "Claro! Jogando a moeda \n\n"
            ),
        },
    }

    #constante para a classe, tomando o nome do canal como parâmetro e setado como variável da instância
    def __init__(self, channel):
        self.channel = channel

    #função para simular o flip da moeda e retornar uma mensagem
    def _flip_coin(self):
        rand_int = random.randint(0,1)
        if rand_int == 0:
            results = "Cara"
        else:
            results = "Coroa"

        texto = f"O resultado é {results}"

        return {"type": "section", "text": {"type": "mrkdwn", "text": texto}},

    # cria e retorna a mensagem
    def cria_mensagem(self):
        return {
            "channel": self.channel,
            "blocks": [
                self.COIN_BLOCK,
                *self._flip_coin(),
            ],
        }

