#weather_telegramm_bot

import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("1879190547:AAHvBHsFdaEMgRei2MgN0iTIibNgXKly9X0")

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('1b24390f0ebd1c6141f87b4738f87c74', config_dict)
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
     bot.reply_to(message, message.text)

if __name__=='__main__':
    bot.infinity_polling()
