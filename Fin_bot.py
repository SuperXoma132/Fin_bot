import telebot
from telebot import types
import sqlite3, time

token = '6996853829:AAHxgnJNE95b3iMk2lhnV9Oxhv_mUQ_fsd4'
bot = telebot.TeleBot(token)
database = sqlite3.connect('database', check_same_thread=False)
cursor = database.cursor()

defoltVariable = "defoltPicture.png"

def bd(message):
    cursor.execute('SELECT user_chat_id FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
    user = cursor.fetchone()
    if not user:
        cursor.execute('INSERT INTO users_fin VALUES(?, ?, ?, ?, ?)', (
        message.chat.id, message.chat.first_name, message.chat.last_name, f'@{message.chat.username}', '0'))
        database.commit()
    else:
        cursor.execute(f'UPDATE users_fin SET user_chat_id=?, user_name=?, user_surname=?, user_username=?, user_budget=? WHERE user_chat_id=?',(message.chat.id, message.chat.first_name, message.chat.last_name, f'@{message.chat.username}', '0', '0'))
        database.commit()

def bd_rub_price_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_budget=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)

def bd_rub_price_select(message):
    try:
        cursor.execute('SELECT user_budget FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def price_rub(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, price_rub)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, price_rub)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, price_rub)
                return
            else:
                bd_rub_price_update(budget, message)
                budget_bd = bd_rub_price_select(message)
                budgetLoans = int(float(budget_bd) * 0.3)
                budgetEat = int(float(budget_bd) * 0.3)
                budgetTransport = int(float(budget_bd) * 0.08)
                budgetInvestment = int(float(budget_bd) * 0.1)
                budgetServices = int(float(budget_bd) * 0.15)
                budgetFun = int(float(budget_bd) * 0.07)
                first = types.InlineKeyboardButton('Попробовать еще 🔄', callback_data='budgetBtn')
                markup.row(first)
                second = types.InlineKeyboardButton('На главную 🏠', callback_data='mainBack')
                markup.row(second)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Ваш бюджет составляет: <b>{budget_bd}</b> рублей.\n\nНаша команда советует вам распределить бюджет следующим образом:\n\nКредиты и ипотеки — 30%: <b>{budgetLoans}</b> рублей\n\nПитание — 30%: <b>{budgetEat}</b> рублей\n\nТранспорт — 8%: <b>{budgetTransport}</b> рублей\n\nИнвестиции — 10%: <b>{budgetInvestment}</b> рублей\n\nЖКХ и связь — 15%: <b>{budgetServices}</b> рублей\n\nРазвлечения — 7%: <b>{budgetFun}</b> рублей', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=["start"])
def start_function(message):
    bd(message)
    markup = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton('Распределить бюджет 💸', callback_data='budgetBtn')
    markup.row(first)
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    bot.send_photo(message.chat.id, file, "<b>Здравствуйте!</b> Я финансовый бот, который поможет вам грамотно распорядиться заработанными деньгами (от студентов РУТ МИИТ)!",reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text', 'voice', 'document', 'photo', 'video', 'video_note', 'sticker'])
def unnecessary_text_function(message):
    markup = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton('Нажми на меня! 😢', callback_data='wellBtn')
    markup.row(first)
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    bot.send_photo(message.chat.id, file,'Не вводи текст, не записывай голосовые сообщения, не отправляй файлы, стикеры, фотографии, видезаписи или видеообращения <b>на страницах, не требующих это!</b>',reply_markup=markup, parse_mode='html')

@bot.callback_query_handler(func=lambda callback: True)
def callback_function(callback):
    if callback.data == 'mainBack':
        bd(callback.message)
        markup = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton('Распределить бюджет 💸', callback_data='budgetBtn')
        markup.row(first)
        file = open(f'./main_photo/{defoltVariable}', 'rb')
        bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
        bot.edit_message_caption("Здравствуйте! Я финансовый бот, который поможет вам грамотно распорядиться заработанными деньгами (от студентов РУТ МИИТ)!", callback.message.chat.id, callback.message.message_id, reply_markup=markup, parse_mode="html")
    if callback.data == 'wellBtn':
            try:
                bot.delete_message(callback.message.chat.id, callback.message.message_id)
                bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
            except:
                bot.send_message(callback.message.chat.id, 'Воспользуйтесь командой /start')
    if callback.data == 'budgetBtn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваш бюджет, чтобы мы распределили его по нашим правилам!',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, price_rub)
