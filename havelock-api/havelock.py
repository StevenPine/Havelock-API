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

#live key below for ticker

key = {'key':'place api key here'}


#symbol abbreviations
#some symbols like '7C' changed because of python quirks

SevenC={'symbol':'7C'}
ALC={'symbol':'ALC'}
AM1={'symbol':'AM1'}
AM100={'symbol':'AM100'}
B_EXCH={'symbol':'B.EXCH'}
B_MINE={'symbol':'B.MINE'}
B_SELL={'symbol':'B.SELL'}
CBTC={'symbol':'CBTC'}
CFIG={'symbol':'CFIG'}
DEALCO={'symbol':'DEALCO'}
HASH={'symbol':'HASH'}
HIF={'symbol':'HIF'}
HMF={'symbol':'HMF'}
MS={'symbol':'MS'}
PETA={'symbol':'PETA'}
RENT={'symbol':'RENT'}
ROCK={'symbol':'ROCK'}
SCRYPT={'symbol':'SCRYPT'}
SF1={'symbol':'SF1'}
SMG={'symbol':'SMG'}

#API commands
#using havelock api documentation.
#https://www.havelockinvestments.com/apidoc.php
#last accessed July 2014

class Havelock:
   def __init__(self, keyname, key):
      self.keyname = keyname
      self.key = key
      self.tickers = []

   def add_ticker(self, ticker):
      self.tickers.append(ticker)

   def ticker(self,symbol):
      try:
         ticker = BASE_URL+'ticker'

         p = requests.post(ticker, symbol)
         data = p.json()
         logging.info(data)
         
         return data

      except ValueError:
         logging.error('Havelock down?')

   def tickerfull(self,symbol):
      try:
         tickerfull = BASE_URL+'tickerfull'

         p = requests.post(tickerfull, symbol)
         data = p.json()
         logging.info(data)
         
         return data

      except ValueError:
         logging.error('Havelock down?')

   def orderbook(self,symbol):
      try:
         orderbook=BASE_URL+'orderbook'

         getorderbook = requests.post(orderbook, symbol)
         data = getorderbook.json()

         return data

      except ValueError:
         logging.error('Havelock down?')

   def orderbookfull(self,symbol):

      try:
         orderbookfull = BASE_URL+'orderbookfull'

         getorderbookfull = requests.post(orderbookfull, symbol)
         data = getorderbookfull.json()
         logging.info(data)

         return data
      
      except ValueError:
         logging.error('Havelock down?')

   def dividendhistory(self,symbol):
      try:
         dividends = BASE_URL+'dividends'

         getdividends = requests.post(dividends, symbol)
         data = getdividends.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

   #Trade History
   #comes with optional dtstart, dtend

   def trade_history(self,symbol,dtstart,dtend):
   #dtstart and end format is yyyy-mm-dd hh:mm:ss
      try:
         payload = {}

         payload['symbol']    = symbol['symbol']
         payload['dtstart']   = str(dtstart)
         payload['dtend']     = str(dtend)

         self.trades(payload)
      
      except ValueError:
         logging.error('Havelock down?')

   def trades(self,payload):   

      try:
         trades = BASE_URL+'trades'

         gettrades = requests.post(trades, payload)
         data = gettrades.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

#Below commands require a API key

   def portfolio(self,key):

      try:
         portfolio = BASE_URL+'portfolio'
         getportfolio = requests.post(portfolio, key)
         data = getportfolio.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

   def balance(self,key):

      try:
         balance = BASE_URL+'balance'
         getbalance = requests.post(balance, key)
         data = getbalance.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')


   def orders(self,key):
   #list open orders

      try:
         orders = BASE_URL+'orders'
         getorders = requests.post(orders, key)
         data = getorders.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')


   def transactions_create(self, key, limit, sort, sinceid, sincets):
   #limit: Maximum number of transactions to fetch (default: 50, maximum: 300)
   #sort: Sort results ASC (Ascending) or DESC (Descending) (default: DESC)
   #sinceid: Show transactions since (but not including) specific id (default: 0)
   #sincets: Show transactions since (and including) specific ts (default: 0)
      
      try:
         payload = {}

         payload['key']    = key['key']
         payload['limit']  = int(limit)
         payload['sort']   = str(sort)
         payload['sinceid']= int(sinceid)
         payload['sincets']= int(sincets)

         self.transactions(payload)

      except ValueError:
         logging.error('Havelock down?')

   def transactions(self,payload):
   #transaction history

      try:
         transactions = BASE_URL+'transactions'
         gettransactions = requests.post(transactions, key)
         data = gettransactions.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')
   #
   #Ensure API key is secure before allowing withdrawals!
   #
   def withdraw(self, payload):
      
      try:
         withdraw = BASE_URL+'withdraw'
         sendwithdraw = requests.post(withdraw, payload)
         data = sendwithdraw.json()
         logging.info(data)

         return data
      
      except ValueError:
         logging.error('Havelock down?')
   
   def withdraw_create(self, key, amount, address):
      try:
         payload = {}

         payload['key']    = key['key']
         payload['amount'] = Decimal(amount)
         payload['address']= str(address)

         self.withdraw(payload)
      
      except ValueError:
         logging.error('Havelock down?')

   def deposit(self, key):
      try:
         getdeposit = requests.post(deposit, key)
         data = getdeposit.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

   def ordercreate(self, payload):
   #payload from build_order

      try:
         ordercreate = BASE_URL+'ordercreate'
         sendordercreate = requests.post(ordercreate, payload)
         data = sendordercreate.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

   def ordercancel(self, payload):
   #takes key and id
   
      try:
         ordercancel = BASE_URL+'ordercancel'
         sendordercancel = requests.post(ordercancel, payload)
         data = sendordercancel.json()
         logging.info(data)

         return data

      except ValueError:
         logging.error('Havelock down?')

   def ordercancel_create(self,key,id):
      
      try:
         payload = {}

         payload['key'] = key['key']
         payload['id']  = int(id)

         self.ordercancel(payload)
      
      except ValueError:
         logging.error('Havelock down?')


   def build_order(self, key, symbol, action, price, units):
   #build the order then send it off to ordercreate
   #eventually you want your bot to create and define the vars in payload for trading

      try:
         payload = {}
         
         payload['key']    = key['key']
         payload['symbol'] = symbol['symbol']
         payload['action'] = str(action)
         payload['price']  = str(price)
         payload['units']  = str(units)
         
         #send payload to ordercreate, this attempts to place an order
         #the bot must process all order responses

         self.ordercreate(payload)

      except ValueError:
         logging.error('Havelock down?')
      except Exception as e:
         logging.info(e)
         logging.info(e.args)
         


"""
The MIT License (MIT)

Copyright (c) <year> <copyright holders>

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
