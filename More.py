import telebot
from telebot import types
import os
import random
from time import sleep


"""Телеграмбот для компании браво """

TOKEN = '6281176698:AAEGRTBKHc4H2sjSqXAofq9qLZzxl-kbhwM'
bot = telebot.TeleBot(TOKEN)

some = os.listdir(path='Photos')

intime = os.listdir(path='Современный')
cla = os.listdir(path='Класика')
sky = os.listdir(path='Скандинав')
# выбираем случайные файлы
num_files = 4  # количество случайных файлов, которые нужно выбрать
random_files = random.sample(some, num_files)

def funk():
    @bot.message_handler(commands=['instagram'])
    def istagram(massage):
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton('Instagram', url=" https://instagram.com/dizainer_azat?igshid=YmMyMTA2M2Y= "))
        bot.send_message(massage.chat.id, 'Отлично, уже открываю...', parse_mode='html', reply_markup=markup)


    @bot.message_handler(commands=['start'])
    def start(massage):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Узнать стоимость проекта онлайн')
        btn2 = types.KeyboardButton('Посмотреть наши интерьеры')
        btn3 = types.KeyboardButton('Из чего состоит дизайн-проект?')
        btn4 = types.KeyboardButton('С чего начинается ремонт?')

        markup.add(btn1, btn2, btn3, btn4)
        send_mess = f'Здравствуйте, {massage.from_user.first_name}, меня зовут Катя \U0001F60A  \nЧем могу вам помочь? '
        bot.send_message(massage.chat.id, send_mess, reply_markup=markup)


    @bot.message_handler(content_types=['text'])
    def price(messege):
        if messege.text == 'Узнать стоимость проекта онлайн':
            markup = types.InlineKeyboardMarkup()
            markup.add()
            markup.add(
                types.InlineKeyboardButton('Хочу узнать цену', url="https://clck.ru/33feT9"))
            bot.send_message(messege.chat.id, 'Отлично! Перейдите в анкету и ответьте на 5 вопросов', parse_mode='html', reply_markup=markup)

                # bot.send_message(messege.chat.id, "Цена +- 30 тысяч рублей за квадратный метр " )
                # bot.send_message(messege.chat.id, "Для более подробной консультации свяжитесь с нашим специалистом по номеру: ")
        elif messege.text == 'Посмотреть наши интерьеры':
            keyboard = types.InlineKeyboardMarkup()
            key_country = types.InlineKeyboardButton(text='Современный стиль', callback_data='Современный стиль')
            keyboard.add(key_country)
            key_apportmant = types.InlineKeyboardButton(text='Классический стиль', callback_data='Классический стиль')
            keyboard.add(key_apportmant)
            key_apportmant = types.InlineKeyboardButton(text='Скандинавский стиль', callback_data='Скандинавский стиль')
            keyboard.add(key_apportmant)
            key_apportmant = types.InlineKeyboardButton(text='Готовые интерьеры', callback_data='Готовые интерьеры')
            keyboard.add(key_apportmant)
            question = 'Выберите стиль?'
            bot.send_message(messege.chat.id, question, reply_markup=keyboard)


        elif messege.text == 'Из чего состоит дизайн-проект?':
            markup = types.InlineKeyboardMarkup()
            markup.add()
            # dok = open('Albom.pdf', 'rb')
            #
            # bot.send_document(messege.chat.id, dok , reply_markup=markup,  timeout=60)
            bot.send_message(messege.chat.id, 'Полный проект состоит из: \n 1. 3D-визуализация \n 2. Рабочие чертежи \n 3. Комплектация с применяемыми материалами \n\n '
                                                  'Всё это позволит начать ремонт с прогнозируемыми расходами и четким тех.заданием. Как? \n '
                                                  'За подробностями обращайтесь к нашему консультанту по номеру:\n +7 987 099 68 14 ',parse_mode='html')
        elif messege.text == 'С чего начинается ремонт?':
            markup = types.InlineKeyboardMarkup()
            markup.add()
            # dok = open('Albom.pdf', 'rb')
            #
            # bot.send_document(messege.chat.id, dok , reply_markup=markup,  timeout=60)
            bot.send_message(messege.chat.id, 'Рад вас видеть!\n\nПрежде чем начнем, пара слов о себе:\n\nМеня зовут Мухаметов Азат \n\n'
                                              '&#9989 Наша студия занимается комплексным ремонтом квартир, начиная с приемки от застройщика и создания дизайн-проекта, до ремонта и комплектации мебелью!\n'
                                              '&#9989 С 2014 Реализовали 50 проектов «под ключ»\n\n'
                                              '&#9989 Наша задача донести до клиента, что ремонт — это легко!\n\n'
                                              'Я покажу вам, как можно сэкономить на Дизайне интерьера и получить продуманный ремонт, которым будут восхищаться ваши родственники и гости. \n\n'
                                              'Читайте следующее сообщение &#128071\n\n'
                                              'https://teletype.in/@masterskayabravo/MoGF8nXXh6G',parse_mode='html')



        else:
            start(messege)


    @bot.callback_query_handler(func=lambda call: True)
    def call_worker(call):
        if call.data == 'Квартира':
            bot.send_message(call.message.chat.id, 'Для квартир у нас такие расценки')
            bot.send_message(call.message.chat.id,
                                 "Для более подробной консультации свяжитесь с нашим специалистом по номеру: ")
        elif call.data == 'Дом':
            bot.send_message(call.message.chat.id, 'Для домов у нас вот такие  расценки')
            bot.send_message(call.message.chat.id, "Для более подробной консультации свяжитесь с нашим специалистом по номеру: ")
        elif call.data == 'Современный стиль':
            #random_files = random.sample(some, num_files)
                # for i in random_files:
                #     photo = open('Photos/' + (i), 'rb')
                #     bot.send_photo(call.message.chat.id, photo)
            media =[]
            for photo in intime:

                file = open('Современный/' + photo, 'rb')
                ab = file.read()
                media.append(telebot.types.InputMediaPhoto(ab))
                file.close()

            bot.send_media_group(call.message.chat.id, media)

        elif call.data == 'Классический стиль':

            media = []
            for photo in cla:
                file = open('Класика/' + photo, 'rb')
                ab = file.read()
                media.append(telebot.types.InputMediaPhoto(ab))
                file.close()

            bot.send_media_group(call.message.chat.id, media)

        elif call.data == 'Скандинавский стиль':
            #bot.send_message(call.message.chat.id, 'Мы для скандинавов не делаем')
            media = []
            for photo in sky:
                file = open('Скандинав/' + photo, 'rb')
                ab = file.read()

                media.append(telebot.types.InputMediaPhoto(ab))
                file.close()

            bot.send_media_group(call.message.chat.id, media)

        elif call.data == 'Готовые интерьеры':

            random_files = random.sample(some, num_files)
            # for i in random_files:
            #     photo = open('Photos/' + (i), 'rb')
            #     bot.send_photo(call.message.chat.id, photo)
            media = []
            for photo in random_files:
                file = open('Photos/' + photo, 'rb')
                ab = file.read()
                media.append(telebot.types.InputMediaPhoto(ab))
                file.close()

            bot.send_media_group(call.message.chat.id, media)


        # @bot.callback_query_handler(func=lambda call: True)
        # def call_jober(call):
        #     if call.data == 'Современный стиль':
        #         random_files = random.sample(some, num_files)
        #         for i in random_files:
        #             photo = open('Photos/' + (i), 'rb')
        #             bot.send_photo(call.message.chat.id, photo)
        #         bot.send_message(call.message.chat.id, 'Правда классно')
        #     elif call.data == 'Старперский стиль':
        #         bot.send_message(call.message.chat.id, 'Мы для старпёров не делаем')

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as _ex:
            print(_ex)
            sleep(15)

try:
    funk()
except Exception:
    funk()
