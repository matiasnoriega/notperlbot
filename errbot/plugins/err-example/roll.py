from errbot import BotPlugin, botcmd
import random

class Roll(BotPlugin):
  
    @botcmd
    def roll(self,msg,args):
        
        numbers = args.split('d',1)

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
