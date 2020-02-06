from errbot import BotPlugin, botcmd


class Roll(BotPlugin):
  
    @botcmd
    def roll(self,msg,args):
        return args.split('d',1)
