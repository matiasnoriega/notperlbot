from errbot import BotPlugin, botcmd
import random
import re


class Roll(BotPlugin):

    @botcmd
    def roll(self, msg, args):

        d = re.match('^[0-9]+d[0-9]+$', args)

        if d:

            numbers = args.split('d', 1)

            if numbers[1] == '0':
                return "la cantidad de caras debe ser un numero distinto de 0"

            dados = int(numbers[0])
            caras = int(numbers[1])
            tirada = ""

            for i in range(dados):
                tirada += str(random.randint(1, caras)) + ' '

            return tirada
        else:
            return "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras"
