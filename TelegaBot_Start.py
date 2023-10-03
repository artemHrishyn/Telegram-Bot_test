import telebot

bot = telebot.TeleBot('1088256853:AAFwP50S5BsVM27Sft67Z3Cxk-yk3e1-cGY')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Добро пожаловать. Рад что вы к нам пожаловали /start')
    bot.send_message(message.chat.id, 'Напиши "Привет"')


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')


bot.polling()