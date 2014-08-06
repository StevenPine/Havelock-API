import willie
import havelock

tickerbot = havelock.Havelock('ticker', 'ticker-key')

@willie.module.commands('havelock')
@willie.module.example('.havelock tickerfull symbol am1')
def havelock(bot, trigger, **kwargs):
   """havelock api commands, syntax is .havelock command key1 value1 key2 value2, etc"""
   irc_input  = trigger.group()
   my_list = irc_input.split()
   
   command = my_list[1]

   
   c = len(my_list)-1
   i = 2
   j = 3
   
   #my ugly list iteration
   while(i<c):
      kwargs[my_list[i]] = my_list[j]
      i = i+1
      j = j+1

   data     = tickerbot.ApiCommand(command, **kwargs)
   data     = str(data)
   
   bot.say(data,max_messages=5)



@willie.module.commands('tickers')
@willie.module.example('.tickers')
def tickers(bot, trigger):
   """lists tickers on havelockinvestments.com"""
   data = tickerbot.tickers
   data = list(data)
   data.sort()
   data = str(data)

   bot.say(data)

