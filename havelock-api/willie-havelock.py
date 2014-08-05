import willie
import havelock
import re

tickerbot = havelock.Havelock('ticker', 'ticker-key')

@willie.module.commands('havelock')

def havelock(bot, trigger, **kwargs):
   
   text  = trigger.group()

   print 'text', text

   my_list = re.split('\W+', str(text))
   print 'my_list', my_list  


   command = my_list[2]
   print 'length', len(my_list)


   kwargs[my_list[3]] = my_list[4]

   print 'command', command
   print 'kwargs', kwargs

   data     = tickerbot.ApiCommand(command, **kwargs)
   data     = str(data)
   
   bot.say(data)



@willie.module.commands('tickers')

def tickers(bot, trigger):
   data = tickerbot.tickers
   data = list(data)
   data.sort()
   data = str(data)

   bot.say(data)


