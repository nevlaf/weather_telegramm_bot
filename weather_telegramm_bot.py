#weather_telegramm_bot

import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru'

owm = OWM('1b24390f0ebd1c6141f87b4738f87c74', config_dict)
bot = telebot.TeleBot("1879190547:AAHvBHsFdaEMgRei2MgN0iTIibNgXKly9X0")

@bot.message_handler(content_types=['text'])
def send_back(message):
#    mgr = owm.weather_manager()
#    observation = mgr.weather_at_place(message.text)
#    w = observation.weather

#    answer = "В городе " + message.text + " сейчас " + w.get_detailed_status() + "\n"
#    answer += "Температура сейчас в районе " + str(temp) + "\n\n"
#        answer = "/help"
#       bot.send_message(message.chat.id, answer)
#        
#    if message.text == "/start":
#        answer = "/start"
#       bot.send_message(message.chat.id, answer)
        
#    if message.text == "/weather":
#        answer = "Уточните город, пожалуйста"
#        bot.send_message(message.chat.id, answer)
            mgr = owm.weather_manager()
            observation = mgr.weather_at_place(message.text)
            w = observation.weather

            answer = "В городе " + message.text + " сейчас " + w.detailed_status + "\n"
#            answer += "Температура сейчас в районе " + w.rain #+ "\n\n"

            bot.send_message(message.chat.id, answer)
        


        
#     bot.reply_to(message, message.text)

if __name__=='__main__':
    bot.infinity_polling()

#mgr = owm.weather_manager()
#place = input("В каком городе?: ")
#observation = mgr.weather_at_place(place)               #('London,GB')
#w = observation.weather

#print(w.detailed_status)         # 'clouds'
#print(w.wind())                  # {'speed': 4.6, 'deg': 330}
#print(w.humidity)                # 87
#print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#print(w.rain)                    # {}
#print(w.heat_index)              # None
#print(w.clouds)                  # 75
