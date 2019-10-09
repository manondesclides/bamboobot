
import requests
import re
import os
from telegram.ext import Updater, CommandHandler



def get_img_url():
    url = ''
    while (os.path.splitext(url)[1] in ['.png', '.jpg', 'jpeg'])==False :
        contents = requests.get('https://random.dog/woof.json').json()    
        url = contents['url']
    return url

def get_gif_url():
    url = ''
    while (os.path.splitext(url)[1] in ['.gif', '.mp4']) ==False :
        contents = requests.get('https://random.dog/woof.json').json()    
        url = contents['url']
    return url

def bop(bot, update):
    url = get_img_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url) 

def bamboo(bot, update):
    url = get_gif_url()
    chat_id = update.message.chat_id
    bot.send_video(chat_id=chat_id, video=url) 

def main():
    updater = Updater('950468208:AAFagenhniR5_QnnIaPbPbiHOSBYmf1brGY')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bamboo',bamboo))
    dp.add_handler(CommandHandler('bop',bop))

    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()
