#instalar 
#pip install pytelegrambotapi

from telebot import TeleBot

BOT_TOKEN = '5957222458:AAEjGY7X99GfPMk9v-i3WJz-V38X8iEbSns'
bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'Olá'])

def send_welcome(message):
    bot.reply_to(message, 'Olá, eu sou o bot de teste do Marcos')
    
@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.infinity_polling()        


