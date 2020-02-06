from errbot import BotPlugin, botcmd


class Roll(BotPlugin):
  
    @botcmd
    def roll(self,msg,args):
        
        numbers = args.split('d',1)

        if not numbers[0].isdigit() == True:
            return "la cantidad de dados debe ser un numero"
        if not numbers[1].isdigit() == True:
            return "la cantidad de caras debe ser un numero"
        dados = int(numbers[0])
        caras = int(numbers[1])