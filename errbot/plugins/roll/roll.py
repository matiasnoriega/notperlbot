from errbot import BotPlugin, botcmd
import random
import re


class Roll(BotPlugin):

    @botcmd
    def roll(self, msg, args):

        d = re.match('^[0-9]+d[0-9]+$', args)
       
        if d:

            numbers = args.split('d', 1)

            if len(numbers) != 2:
                return "poneme la cantidad de caras del dado, no soy mago"
            if not numbers[0].isdigit() == True:
                return "la cantidad de dados debe ser un numero"
            if not numbers[1].isdigit() == True or numbers[1] == '0':
                return "la cantidad de caras debe ser un numero distinto de 0"

            dados = int(numbers[0])
            caras = int(numbers[1])
            tirada = ""

            for i in range(dados):
                tirada += str(random.randint(1, caras)) + ' '

            return tirada
        else:
            return "el formato es '!roll XdY', donde X es la cantidad de dados e Y la cantidad de caras"
