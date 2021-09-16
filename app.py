import os
Active_key = os.getenv('Active_Key')
Username = os.getenv('Username')

from telegram.ext import Updater, MessageHandler, Filters

from Adafruit_IO import Client
 
aio = Client(Username,Active_key)
 
def sayan1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned on')
  aio.send('major-2',1)
 
def sayan2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned off')
  aio.send('major-2',0)
 
def sayan3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')
  aio.send('major-2',2)
 
def sayan4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')
  aio.send('major-2',4)
 
 
def main(bot,update):
  a= bot.message.text.lower()
  
  if a =="turn on light":
    sayan1(bot,update)
  elif a =="turn off light":
    sayan2(bot,update)
  elif a =="turn on fan":
    sayan3(bot,update)
  elif a =="turn off fan":
    sayan4(bot,update) 
     
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
