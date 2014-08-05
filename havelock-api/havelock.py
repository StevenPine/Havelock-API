#Simple Havelock logging and access tool
#Using requests 

import requests
import json
import time
import logging

from decimal import *

from datetime import datetime
#this has a bunch of stuff, I just want a TIMESTAMP

#make sure havelock.log exists
logging.basicConfig(
   filename='havelock.log', 
   level=logging.DEBUG, 
   format='%(asctime)s:%(levelname)s:%(message)s')

DEBUG=True
BASE_URL='https://www.havelockinvestments.com/r/'


logging.info('Running sample Havelock logging and API')
logging.info('DEBUG %s', DEBUG)


#API commands
#using havelock api documentation.
#https://www.havelockinvestments.com/apidoc.php
#last accessed July 2014

class Havelock:
   def __init__(self, keyname, key):
      self.keyname = keyname
      self.key = key
      
      self.tickers = {}

      data = self.ApiCommand('ticker')
      tickers = list(data)
      tickers.sort()
      i = 0

      while i < len(tickers):
         self.tickers[str(tickers[i])]= {'symbol':str(tickers[i])}
         i=i+1
      
   def ApiCommand(self, command, **kwargs):
      

      commands = {}

      commands['ticker']            = {'symbol':''}
      commands['tickerfull']        = {'symbol':''}
      commands['orderbook']         = {'symbol':''}
      commands['orderbookfull']     = {'symbol':''}
      commands['dividends']         = {'symbol':''}
      commands['trades']            = {'symbol':'','dtstart':'yyyy-mm-dd hh:mm:ss','dtend':'yyyy-mm-dd hh:mm:ss'}
      commands['portfolio']         = {'key':''}
      commands['balance']           = {'key':''}
      commands['orders']            = {'key':''}
      commands['transactions']      = {'key':'','limit':'','sort':'','sinceid':'','sincets':''}
      commands['withdraw']          = {'key':'','amount':'','address':''}
      commands['deposit']           = {'key':''}
      commands['ordercreate']       = {'key':'','symbol':'','action':'buy or sell','price':'','units':''}
      commands['cancelorder']       = {'key':'','id':''}
      
      try:

         if(command in commands):
            commands[command] = kwargs

            p = requests.post(BASE_URL+command, commands[command])
            data = p.json()
            logging.info(data)

            return data
            
      except ValueError:
         logging.error('Havelock down?')


"""
The MIT License (MIT)

Copyright (c) 2014 Steven Lee BilloPine

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

#END
