
import requests
import re
from telegram.ext import Updater, CommandHandler


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bamboo(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url) 


def main():
    updater = Updater('950468208:AAFagenhniR5_QnnIaPbPbiHOSBYmf1brGY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bamboo',bamboo))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
