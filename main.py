import telebot
import os
from dotenv import load_dotenv
from telebot import types

load_dotenv()

token_user = os.getenv('TOKEN')
url_dvorik = os.getenv('urlDvorik')
url_shop = os.getenv('urlShopDvorik')
url_VK = os.getenv('urlVK')
number_Nellia = os.getenv('numberNellia')
number_Irina = os.getenv('numberIrina')
number_Valentina = os.getenv('numberValentina')
number_Alla = os.getenv('numberAlla')
Price_Programing_Text = os.getenv('PriceProgramingText')
Price_Robotics_Text = os.getenv('PriceRoboticsText')
Price_SpeechTherapist_Text = os.getenv('PriceSpeechTherapistText')
Price_Other_Text = os.getenv('PriceOtherText')
About_Us = os.getenv('AboutUs')

bot = telebot.TeleBot(token_user)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt_sign_up_for_a_class = types.KeyboardButton('Записаться на занятие')
    bt_site = types.KeyboardButton('Узнать цены')
    bt_shop = types.KeyboardButton('Группа ВК')
    bt_about_us = types.KeyboardButton('О нас')
    markup.row(bt_sign_up_for_a_class, bt_site)
    markup.row(bt_shop, bt_about_us)
    bot.send_message(message.chat.id, f'Привет {message.from_user.username} чем могу помочь?', reply_markup=markup)


@bot.message_handler()
def info_button(message):
    if message.text == 'Записаться на занятие':
        file_image = open("./Image_1.jpeg", "rb")
        bot.send_photo(message.chat.id, file_image)
        bot.send_message(message.chat.id, f"Нелля Александровна: {number_Nellia}")
        bot.send_message(message.chat.id, f"Ирина Владиславовна: {number_Irina}")
        bot.send_message(message.chat.id, f"Валентина Анатольевна: {number_Valentina}")
        bot.send_message(message.chat.id, f"Алла Анатольевна: {number_Alla}")
    elif message.text == 'Узнать цены':
        markup_price = types.InlineKeyboardMarkup()
        btRobotics = types.InlineKeyboardButton('Робототехника', callback_data='Robotics')
        btSpeechTherapist = types.InlineKeyboardButton('Логопед', callback_data='SpeechTherapist')
        btProgramming = types.InlineKeyboardButton('Программирование', callback_data='Programming')
        btOther = types.InlineKeyboardButton('Другое', callback_data='Other')
        markup_price.row(btRobotics, btProgramming)
        markup_price.row(btSpeechTherapist, btOther)
        bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup_price)

        @bot.callback_query_handler(func=lambda callback: True)
        def callback_price_message(callback):
            if callback.data == 'Robotics':
                file_image_Robotics = open('Robote.jpg', 'rb')
                bot.send_photo(callback.message.chat.id, file_image_Robotics)
                bot.send_message(callback.message.chat.id, Price_Robotics_Text)
            elif callback.data == 'Programming':
                file_image_Programming = open('Program.webp', 'rb')
                bot.send_photo(callback.message.chat.id, file_image_Programming)
                bot.send_message(callback.message.chat.id, Price_Programing_Text)
            elif callback.data == 'SpeechTherapist':
                file_image_SpeechTherapist = open('SpeechTherapist.webp', 'rb')
                bot.send_photo(callback.message.chat.id, file_image_SpeechTherapist)
                bot.send_message(callback.message.chat.id, Price_SpeechTherapist_Text)
            elif callback.data == 'Other':
                bot.send_message(callback.message.chat.id, Price_Other_Text)
    elif message.text == 'Группа ВК':
        bot.send_message(message.chat.id, f'ВК: {url_VK}')
    elif message.text == 'О нас':
        bot.send_message(message.chat.id, About_Us)


bot.polling(non_stop=True)
