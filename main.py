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
        cursor.execute('INSERT INTO users_fin VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (
        message.chat.id, message.chat.first_name, message.chat.last_name, f'@{message.chat.username}', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '))
        database.commit()
    else:
        cursor.execute(f'UPDATE users_fin SET user_chat_id=?, user_name=?, user_surname=?, user_username=?, user_budget=?, user_mortgage=?, user_eat=?, user_services=?, user_entert=?, user_education=?, user_accumulation=?, user_credit=?, user_investment=?, user_message=?  WHERE user_chat_id=?',(message.chat.id, message.chat.first_name, message.chat.last_name, f'@{message.chat.username}', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', ' '))
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

def bd_mortgage_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_mortgage=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_mortgage_select(message):
    try:
        cursor.execute('SELECT user_mortgage FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_eat_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_eat=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_eat_select(message):
    try:
        cursor.execute('SELECT user_eat FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_services_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_services=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_services_select(message):
    try:
        cursor.execute('SELECT user_services FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_entert_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_entert=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_entert_select(message):
    try:
        cursor.execute('SELECT user_entert FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_education_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_education=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_education_select(message):
    try:
        cursor.execute('SELECT user_education FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_accumulation_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_accumulation=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_accumulation_select(message):
    try:
        cursor.execute('SELECT user_accumulation FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_credit_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_credit=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_credit_select(message):
    try:
        cursor.execute('SELECT user_credit FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_investment_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_investment=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_investment_select(message):
    try:
        cursor.execute('SELECT user_investment FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
        VariableList = cursor.fetchall()
        for i in VariableList:
            for Variable in i:
                return Variable if Variable is not None else None
    except:
        bd_rub_price_select(message)

def bd_message_update(main ,message):
    Variable = main
    try:
        cursor.execute(f'UPDATE users_fin SET user_message=? WHERE user_chat_id=?', (Variable, message.chat.id,))
        database.commit()
    except:
        bd_rub_price_update(Variable, message)
def bd_message_select(message):
    try:
        cursor.execute('SELECT user_message FROM users_fin WHERE user_chat_id=?', (message.chat.id,))
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
                budgetMortgage = int(float(budget_bd) * 0.25)
                budgetEat = int(float(budget_bd) * 0.15)
                budgetServices = int(float(budget_bd) * 0.1)
                budgetEntert = int(float(budget_bd) * 0.08)
                budgetEducation = int(float(budget_bd) * 0.1)
                budgetAccumulation = int(float(budget_bd) * 0.12)
                budgetCredit = int(float(budget_bd) * 0.12)
                budgetInvestment = int(float(budget_bd) * 0.08)
                first = types.InlineKeyboardButton('Попробовать еще 🔄', callback_data='budgetBtn')
                markup.row(first)
                third = types.InlineKeyboardButton('Что за метод? 🎓', url='http://www.lookatme.ru/mag/people/experience/209369-alexa-von-tobel')
                markup.row(third)
                fourth = types.InlineKeyboardButton('Как инвестировать? 💸',url='https://www.sravni.ru/text/kakie-akczii-sovetuyut-kupit-v-2024-godu/')
                markup.row(fourth)
                second = types.InlineKeyboardButton('На главную 🏠', callback_data='mainBack')
                markup.row(second)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Ваш бюджет составляет: <b>{budget_bd}</b> рублей.\n\nНаша команда советует вам распределить бюджет по принципу 50/20/30 (метод знаменитой женщины предпринимателя — Алексы фон Тобель):\n\n\n<b>1) Обязательные расходы 50%:</b>\n\n\nИпотека — 25%: <b>{budgetMortgage}</b> рублей\n\nЕда — 15%: <b>{budgetEat}</b> рублей\n\nОбязательные услуги — 10%: <b>{budgetServices}</b> рублей\n\n\n<b>2) Инвестиции в будущее 20%:</b>\n\n\nКредит  — 12%: <b>{budgetCredit}</b> рублей\n\nИвестиции  — 8%: <b>{budgetInvestment}</b> рублей\n\n\n<b>3) Необязательные траты 30%:</b>\n\n\nРазвлечения — 8%: <b>{budgetEntert}</b> рублей\n\nОбразование — 10%: <b>{budgetEducation}</b> рублей\n\nСвободные деньги/накопления — 12%: <b>{budgetAccumulation}</b> рублей', reply_markup=markup, parse_mode='html')
def mortgage_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, mortgage_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, mortgage_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, mortgage_func)
                return
            else:
                bd_mortgage_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget22Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def eat_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, eat_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, eat_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, eat_func)
                return
            else:
                bd_eat_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget23Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def services_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, services_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, services_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, services_func)
                return
            else:
                bd_services_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget24Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def credit_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, credit_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, credit_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, credit_func)
                return
            else:
                bd_credit_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget25Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def investment_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, investment_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, investment_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, investment_func)
                return
            else:
                bd_investment_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget26Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def entert_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, entert_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, entert_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, entert_func)
                return
            else:
                bd_entert_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget27Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def education_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, education_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, education_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, education_func)
                return
            else:
                bd_education_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget28Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к следующему шагу!', reply_markup=markup, parse_mode='html')
def accumulation_func(message):
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    markup = types.InlineKeyboardMarkup()
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    elif message.content_type == 'document':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    elif message.content_type == 'video_note':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    elif message.content_type == 'sticker':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    elif message.content_type == 'video':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!',parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    elif message.content_type == 'photo':
        bot.send_photo(message.chat.id, file,f'Ошибка типа данных сообщения! Введи текст!', parse_mode='html')
        bot.register_next_step_handler(message, accumulation_func)
    if message.content_type == 'text':
        if message.text == r'/start':
            start_function(message)
        else:
            try:
                budget = int(message.text)
            except ValueError:
                bot.send_photo(message.chat.id, file,f'Ошибка (сообщение не является числом)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, accumulation_func)
                return
            if budget <= 0:
                bot.send_photo(message.chat.id, file,f'Ошибка (цена ≤ 0)! Попробуйте еще раз!',reply_markup=markup, parse_mode='html')
                bot.register_next_step_handler(message, accumulation_func)
                return
            else:
                bd_accumulation_update(budget, message)
                first = types.InlineKeyboardButton('Следующий шаг! 📌', callback_data='budget3Btn')
                markup.row(first)
                file2 = open(f'./main_photo/{defoltVariable}', 'rb')
                bot.send_photo(message.chat.id, file2, f'Давайте перейдем к итогу!', reply_markup=markup, parse_mode='html')

@bot.message_handler(commands=["start"])
def start_function(message):
    bd(message)
    bd_message_update(' ', message)
    markup = types.InlineKeyboardMarkup()
    first = types.InlineKeyboardButton('Распределить быстро 💰', callback_data='budgetBtn')
    markup.row(first)
    second = types.InlineKeyboardButton('Распределить детально 💸', callback_data='budget21Btn')
    markup.row(second)
    file = open(f'./main_photo/{defoltVariable}', 'rb')
    bot.send_photo(message.chat.id, file, "<b>Здравствуйте!</b> Я финансовый бот, который поможет вам грамотно распределить бюджет (от студентов РУТ МИИТ)!",reply_markup=markup, parse_mode='html')
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
        bd_message_update(' ', callback.message)
        markup = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton('Распределить быстро 💰', callback_data='budgetBtn')
        markup.row(first)
        second = types.InlineKeyboardButton('Распределить детально 💸', callback_data='budget21Btn')
        markup.row(second)
        file = open(f'./main_photo/{defoltVariable}', 'rb')
        bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
        bot.edit_message_caption("Здравствуйте! Я финансовый бот, который поможет вам грамотно распределить бюджет (от студентов РУТ МИИТ)!", callback.message.chat.id, callback.message.message_id, reply_markup=markup, parse_mode="html")
    if callback.data == 'mainBack2':
        bd(callback.message)
        bd_message_update(' ', callback.message)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        markup = types.InlineKeyboardMarkup()
        first = types.InlineKeyboardButton('Распределить быстро 💰', callback_data='budgetBtn')
        markup.row(first)
        second = types.InlineKeyboardButton('Распределить детально 💸', callback_data='budget21Btn')
        markup.row(second)
        file = open(f'./main_photo/{defoltVariable}', 'rb')
        bot.send_photo(callback.message.chat.id, file,"<b>Здравствуйте!</b> Я финансовый бот, который поможет вам грамотно распределить бюджет (от студентов РУТ МИИТ)!",reply_markup=markup, parse_mode='html')

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

    if callback.data == 'budget21Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на ИПОТЕКУ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, mortgage_func)
    if callback.data == 'budget22Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на ЕДУ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, eat_func)
    if callback.data == 'budget23Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на ОБЯЗАТЕЛЬНЫЕ УСЛУГИ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, services_func)
    if callback.data == 'budget24Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на КРЕДИТ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, credit_func)
    if callback.data == 'budget25Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на ИНВЕСТИЦИИ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, investment_func)
    if callback.data == 'budget26Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на РАЗВЛЕЧЕНИЯ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, entert_func)
    if callback.data == 'budget27Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите ваши траты в месяц на ОБРАЗОВАНИЕ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, education_func)
    if callback.data == 'budget28Btn':
            markup = types.InlineKeyboardMarkup()
            file = open(f'./main_photo/{defoltVariable}', 'rb')
            bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
            bot.edit_message_caption(f'Пожалуйста, введите сколько вы можете откладывать на СВОБОДНЫЕ ДЕНЬГИ/НАКОПЛЕНИЯ:',callback.message.chat.id,callback.message.message_id, reply_markup=markup, parse_mode="html")
            bot.register_next_step_handler(callback.message, accumulation_func)

    if callback.data == 'budget3Btn':

        #Доход человека
        budgetMortgage = int(bd_mortgage_select(callback.message))
        budgetEat = int(bd_eat_select(callback.message))
        budgetServices = int(bd_services_select(callback.message))
        budgetEntert = int(bd_entert_select(callback.message))
        budgetEducation = int(bd_education_select(callback.message))
        budgetAccumulation = int(bd_accumulation_select(callback.message))
        budgetCredit = int(bd_credit_select(callback.message))
        budgetInvestment = int(bd_investment_select(callback.message))

        sum_budget = budgetMortgage + budgetEat + budgetServices + budgetEntert + budgetEducation + budgetAccumulation + budgetCredit + budgetInvestment

        #Доход человека в процентах
        budgetMortgageProc = int(round((budgetMortgage / sum_budget), 2) * 100)
        budgetEatProc = int(round((budgetEat / sum_budget), 2) * 100)
        budgetServicesProc = int(round((budgetServices / sum_budget), 2) * 100)
        budgetEntertProc = int(round((budgetEntert / sum_budget), 2) * 100)
        budgetEducationProc = int(round((budgetEducation / sum_budget), 2) * 100)
        budgetAccumulationProc = int(round((budgetAccumulation / sum_budget), 2) * 100)
        budgetCreditProc = int(round((budgetCredit / sum_budget), 2) * 100)
        budgetInvestmentProc = int(round((budgetInvestment / sum_budget), 2) * 100)

        #Рекомендации
        _budgetMortgage = int(float(sum_budget) * 0.25)
        _budgetEat = int(float(sum_budget) * 0.15)
        _budgetServices = int(float(sum_budget) * 0.1)
        _budgetEntert = int(float(sum_budget) * 0.08)
        _budgetEducation = int(float(sum_budget) * 0.1)
        _budgetAccumulation = int(float(sum_budget) * 0.12)
        _budgetCredit = int(float(sum_budget) * 0.12)
        _budgetInvestment = int(float(sum_budget) * 0.08)

        markup = types.InlineKeyboardMarkup()
        file = open(f'./main_photo/{defoltVariable}', 'rb')
        bot.edit_message_media(types.InputMediaPhoto(file), callback.message.chat.id, callback.message.message_id)
        bot.edit_message_caption(f"Ваш бюджет составляет: <b>{sum_budget}</b> рублей.\n\n<b>Вы РАСПРЕДЕЛИЛИ бюджет следующим образом:</b>\n\nИпотека — {budgetMortgageProc}%: <b>{budgetMortgage}</b> рублей\n\nЕда — {budgetEatProc}%: <b>{budgetEat}</b> рублей\n\nОбязательные услуги — {budgetServicesProc}%: <b>{budgetServices}</b> рублей\n\nКредит  — {budgetCreditProc}%: <b>{budgetCredit}</b> рублей\n\nИвестиции  — {budgetInvestmentProc}%: <b>{budgetInvestment}</b> рублей\n\nРазвлечения — {budgetEntertProc}%: <b>{budgetEntert}</b> рублей\n\nОбразование — {budgetEducationProc}%: <b>{budgetEducation}</b> рублей\n\nСвободные деньги/накопления — {budgetAccumulationProc}%: <b>{budgetAccumulation}</b> рублей\n\n\n<b>Наша команда СОВЕТУЕТ вам распределить бюджет по принципу 50/20/30 (метод знаменитой женщины предпринимателя — Алексы фон Тобель):</b>\n\n<b>1) Обязательные расходы 50%:</b>\n\nИпотека — 25%: <b>{_budgetMortgage}</b> рублей\n\nЕда — 15%: <b>{_budgetEat}</b> рублей\n\nОбязательные услуги — 10%: <b>{_budgetServices}</b> рублей\n\n<b>2) Инвестиции в будущее 20%:</b>\n\nКредит  — 12%: <b>{_budgetCredit}</b> рублей\n\nИвестиции  — 8%: <b>{_budgetInvestment}</b> рублей\n\n<b>3) Необязательные траты 30%:</b>\n\nРазвлечения — 8%: <b>{_budgetEntert}</b> рублей\n\nОбразование — 10%: <b>{_budgetEducation}</b> рублей\n\nСвободные деньги/накопления — 12%: <b>{_budgetAccumulation}</b> рублей",callback.message.chat.id, callback.message.message_id, reply_markup=markup, parse_mode="html")


        if abs(25 - budgetMortgageProc) >= 5:
            message_text = bd_message_select(callback.message)
            message_text += 'Рассмотрите возможность рефинансирования ипотеки для снижения ежемесячных платежей.'
            bd_message_update(message_text, callback.message)

        if abs(15 - budgetEatProc) >= 5:
            if budgetEatProc >= 15:
                message_text = bd_message_select(callback.message)
                message_text += 'Попробуйте составить более экономичный план питания.'
                bd_message_update(message_text, callback.message)
        if abs(10 - budgetServicesProc) >= 5:
            if budgetServicesProc >= 10:
                message_text = bd_message_select(callback.message)
                message_text += 'Проверьте ваши счета за услуги на предмет возможных сбережений.'
                bd_message_update(message_text, callback.message)
        if abs(8 - budgetEntertProc) >= 5:
            if budgetEntertProc >= 8:
                message_text = bd_message_select(callback.message)
                message_text += 'Попробуйте найти более дешевые или бесплатные способы развлечения.'
                bd_message_update(message_text, callback.message)
        if abs(10 - budgetEducationProc) >= 5:
            if budgetEducationProc >= 10:
                message_text = bd_message_select(callback.message)
                message_text += 'Ищите возможности для сокращения расходов на образование, возможно, есть более доступные курсы или программы.'
                bd_message_update(message_text, callback.message)
            elif budgetEducationProc <= 10:
                message_text = bd_message_select(callback.message)
                message_text += 'Вы можете потратить свободные деньги на образование.'
                bd_message_update(message_text, callback.message)
        if abs(12 - budgetAccumulationProc) >= 5:
            if budgetAccumulationProc <= 12:
                message_text = bd_message_select(callback.message)
                message_text += 'У вас мало накоплений, старайтесь больше откладывать.'
                bd_message_update(message_text, callback.message)
            elif budgetAccumulationProc >= 12:
                message_text = bd_message_select(callback.message)
                message_text += 'Инвестируйте часть ваших накоплений.'
                bd_message_update(message_text, callback.message)
        if abs(12 - budgetCreditProc) >= 5:
            if budgetCreditProc >= 12:
                message_text = bd_message_select(callback.message)
                message_text += 'Попробуйте сконсолидировать ваши кредиты или пересмотрите условия погашения.'
                bd_message_update(message_text, callback.message)
            elif budgetCreditProc <= 12:
                message_text = bd_message_select(callback.message)
                message_text += 'Инвестируйте деньги, которые вы не используйте для погашения долгов.'
                bd_message_update(message_text, callback.message)
        if abs(8 - budgetInvestmentProc) >= 5:
            if budgetInvestmentProc <= 8:
                message_text = bd_message_select(callback.message)
                message_text += 'Постарайтесь больше инвестировать.'
                bd_message_update(message_text, callback.message)

        messageTextItog = bd_message_select(callback.message)
        if messageTextItog == ' ':
            markup = types.InlineKeyboardMarkup()
            third = types.InlineKeyboardButton('Что за метод? 🎓',url='http://www.lookatme.ru/mag/people/experience/209369-alexa-von-tobel')
            markup.row(third)
            fourth = types.InlineKeyboardButton('Как инвестировать? 💸',url='https://www.sravni.ru/text/kakie-akczii-sovetuyut-kupit-v-2024-godu/')
            markup.row(fourth)
            first = types.InlineKeyboardButton('Вернуться домой 🏠', callback_data='mainBack2')
            markup.row(first)
            bot.send_message(callback.message.chat.id, "У вас всё хорошо с рапределением бюджета)", reply_markup=markup)
        else:
            markup = types.InlineKeyboardMarkup()
            third = types.InlineKeyboardButton('Что за метод? 🎓',url='http://www.lookatme.ru/mag/people/experience/209369-alexa-von-tobel')
            markup.row(third)
            fourth = types.InlineKeyboardButton('Как инвестировать? 💸',url='https://www.sravni.ru/text/kakie-akczii-sovetuyut-kupit-v-2024-godu/')
            markup.row(fourth)
            first = types.InlineKeyboardButton('Вернуться домой 🏠', callback_data='mainBack2')
            markup.row(first)
            messageTextItog = bd_message_select(callback.message)
            bot.send_message(callback.message.chat.id, messageTextItog, reply_markup=markup)

while True:
    try:
        bot.polling(none_stop=True)
    except:
        time.sleep(5)