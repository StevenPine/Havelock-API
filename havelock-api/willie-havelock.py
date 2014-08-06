import willie
import havelock
import re

tickerbot = havelock.Havelock('ticker', 'ticker-key')

@willie.module.commands('havelock')

def havelock(bot, trigger, **kwargs):
   
   irc_input  = trigger.group()


   my_list = irc_input.split()
   
   
   command = my_list[1]

   c = len(my_list)-1

   i = 2
   j = 3
   
   while(i<c):
      kwargs[my_list[i]] = my_list[j]
      i = i+1
      j = j+1

   data     = tickerbot.ApiCommand(command, **kwargs)
   data     = str(data)
   
   bot.say(data,max_messages=5)



@willie.module.commands('tickers')

def tickers(bot, trigger):
   data = tickerbot.tickers
   data = list(data)
   data.sort()
   data = str(data)

   bot.say(data)


