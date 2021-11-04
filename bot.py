import telebot
import config
import txt

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):

    start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Хочу знать!")
    item2 = types.KeyboardButton("Не интересно")

    start_markup.add(item1,item2)

    bot.send_message(message.chat.id, txt.start_text.format(message.from_user, bot.get_me()), 
                     parse_mode='html', reply_markup=start_markup)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
   
    if message.text == 'Не интересно' or message.text == 'Никакая':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Все таки хочу знать...")
        item2 = types.KeyboardButton("Пожалуй да")
        markup.add(item1,item2)

        bot.send_message(message.chat.id, "Что ж, в другой раз", reply_markup=markup)

    elif message.text == 'Хочу знать!' or message.text == 'Все таки хочу знать...' or message.text == 'К теме':

        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Понял принял', reply_markup=a)

        markup = types.InlineKeyboardMarkup(row_width=4)
        dev_1 = types.InlineKeyboardButton(text='1', callback_data='1')
        dev_2 = types.InlineKeyboardButton(text='2', callback_data='2')
        dev_3 = types.InlineKeyboardButton(text='3', callback_data='3')
        dev_4 = types.InlineKeyboardButton(text='4', callback_data='4')
        
        
        item5 = types.InlineKeyboardButton(text='Кратко про сферы разработки', callback_data='Кратко про сферы разработки')
        item0 = types.InlineKeyboardButton(text='Никакая', callback_data='Никакая')

        markup.add(dev_1, dev_2, dev_3, dev_4)
        markup.add(item5)
        markup.add(item0)
        bot.send_message(message.chat.id, txt.wnatKnow, reply_markup=markup)

    elif  message.text == "Назад к сферам":
        a = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Супер!', reply_markup=a)

        markup = types.InlineKeyboardMarkup(row_width=4)
        dev_1 = types.InlineKeyboardButton(text='1', callback_data='1')
        dev_2 = types.InlineKeyboardButton(text='2', callback_data='2')
        dev_3 = types.InlineKeyboardButton(text='3', callback_data='3')
        dev_4 = types.InlineKeyboardButton(text='4', callback_data='4')
        
        
        item5 = types.InlineKeyboardButton(text='Кратко про сферы разработки', callback_data='Кратко про сферы разработки')
        item0 = types.InlineKeyboardButton(text='Никакая', callback_data='Никакая')

        markup.add(dev_1, dev_2, dev_3, dev_4)
        markup.add(item5)
        markup.add(item0)
        bot.send_message(message.chat.id, txt.wnatKnowAfter, reply_markup=markup)

    elif  message.text == "Привет" or message.text == "Хай":
        
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("К теме")
        markup.add(item)
        bot.send_message(message.chat.id, "Привет, жми на кнопку внизу", reply_markup=markup)

    elif  message.text == "Как дела?" or message.text == "Как дела":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("К теме")
        markup.add(item)
        bot.send_message(message.chat.id, "Потихоньку, помаленьку, ты как?", reply_markup=markup)

    elif  message.text == "Плохо" or message.text == "Нормально":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("К теме")
        markup.add(item)
        bot.send_message(message.chat.id, "Все будет супер!", reply_markup=markup)

    elif  message.text == "Хорошо" or message.text == "Отлично":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item = types.KeyboardButton("К теме")
        markup.add(item)
        bot.send_message(message.chat.id, "Вот и славно!", reply_markup=markup)

    else: bot.send_message(message.chat.id, "Ну шо тут сказати, не знаю что тут и ответить")


@bot.callback_query_handler(func=lambda call: True)
def callback_dev(call):
    if call.data == "1": 

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, txt.web_dev,parse_mode='html',reply_markup=markup)

    elif call.data == "2":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, txt.game_dev,parse_mode='html',reply_markup=markup)
        
    elif call.data == "3":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, txt.android_dev,parse_mode='html',reply_markup=markup)

    elif call.data == "4":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, txt.soft_dev,parse_mode='html',reply_markup=markup)

    elif call.data == "Кратко про сферы разработки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, "Сферы разработки еще в разработке)",parse_mode='html',reply_markup=markup)

    elif call.data == "Никакая":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        item = types.KeyboardButton("Назад к сферам")
        markup.add(item)

        bot.send_message(call.message.chat.id, "Ну, в другой раз",parse_mode='html',reply_markup=markup)


#Launch
bot.polling(none_stop = True)
