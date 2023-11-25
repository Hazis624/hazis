import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import random
import time
token = '6845562531:AAGUxbT1pwVoT8yqkBmyIrj5KdJpXGLcr2U'
bot = telebot.TeleBot(token)

@bot.message_handler(commands = ['start','help'])
def send_welcome(message,res = False):
    welcome_text = """    Привет!Я знаю много интересных фактов и могу отправлять разные фотографии.    """
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 1,resize_keyboard = True,one_time_keyboard = False)
    button1 = telebot.types.KeyboardButton('Факт')
    button2 = telebot.types.KeyboardButton('Стих')
    button3 = telebot.types.KeyboardButton('Мотивация на каждый день')
    button4 = telebot.types.KeyboardButton('Стикер')
    button5 = telebot.types.KeyboardButton('Игра')
    keyboard.add(button1,button2,button3,button4,button5)
    bot.send_message(message.chat.id,welcome_text,reply_markup=keyboard)
@bot.message_handler(commands = ['poem'])
def send_poem(message):
    poem_text = """    Я помню чудное мгновенье...    """
    bot.send_message(message.chat.id,poem_text)
    keyboard = telebot.types.InlineKeyboardMarkup(row_width = 1)
    button_url = telebot.types.InlineKeyboardButton('Перейти',url = 'https://stihi.ru/')
    keyboard.add(button_url)
    bot.send_message(message.chat.id,'Больше стихов по ссылке ниже',reply_markup=keyboard)
@bot.message_handler(commands = ['fact'])
def send_fact(message):
    response = requests.get('https://i-fakt.ru/')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    facts = html.find_all(class_ = "p-2 clearfix")
    fact = random.choice(facts)
    fact_link = fact.a.attrs['href']
    fact_text = fact.text
    bot.send_message(message.chat.id, fact_link + fact_text)
@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id,'CAACAgEAAxkBAAEHC8FjrH6-fLKWFqJfgCYrf2kvN76nKAACbwIAAgTo8UZ6rfgCseDN8ywE')
@bot.message_handler(commands=['motivation'])
def send_motiv(message):
    bot.send_message(message.chat.id, 'Привет! Я буду присылать тебе напоминание каждый день.')
    while True:
        now = time.localtime()
        motivate_list = ['Верь в себя, и все возможно!','Сегодня твой день, сделай его замечательным!'
                         'Жизнь – это театр, и каждый из нас актер.','Стремись к успеху, а не к совершенству.',
                         'Никогда не сдавайся, даже если все кажется безнадежным.','Лучший способ предсказать будущее – создать его самому.',
                         'Не останавливайся, пока не почувствуешь гордость.','Чем сильнее ваши испытания, тем значительнее ваши победы.',
                         'Я хочу, могу и заслуживаю этого.','Будьте «лишним» в экстраординарном.',
                         'Тебе достаточно быть таким, какой ты есть.',
                         'Никто не может заставить вас чувствовать себя неполноценным без вашего согласия.',
                         'Будьте героиней своей жизни, а не жертвой.',
                         'Вы невероятные, могущественные и замечательные, позвольте другим увидеть всю вашу ценность.',
                         'Никогда не поздно стать тем, кем ты мог бы стать.',
                         'Чтобы начать, не обязательно быть большим. Но чтобы стать великим, нужно начать.',
                         'Если ты упал вчера, встань сегодня.',
                         'У вас есть возможность создать жизнь своей мечты.',
                         'Что тебя не убивает, то делает тебя сильнее.',
                         'Вопрос не в том, кто мне позволит это сделать, а в том, кто сможет меня остановить.']
        if now.tm_hour == 16 and now.tm_min == 57:
            bot.send_message(message.chat.id,random.choice(motivate_list))
        else:
            continue
        time.sleep(60)


@bot.message_handler(commands =['play'])
def send_play(message,res = False):
    keyboard1 = telebot.types.ReplyKeyboardMarkup(row_width = 1,resize_keyboard = True,one_time_keyboard = False)
    button_1 = telebot.types.KeyboardButton('Экшен')
    button_2 = telebot.types.KeyboardButton('Выживание')
    button_3 = telebot.types.KeyboardButton('Страшное выживание')
    button_4 = telebot.types.KeyboardButton('Королевская битва')
    keyboard1.add(button_1,button_2,button_3,button_4)
    bot.send_message(message.chat.id,'Выберите жанр',reply_markup=keyboard1)
def set_ekshen(message):
    response = requests.get('https://vgtimes.ru/games/genres/ekshen/#gb_top')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    plays = html.find_all(class_ = "title")
    play = random.choice(plays)
    play_text1 = play.text
    bot.send_message(message.chat.id,play_text1)
def set_survive(message):
    response = requests.get('https://vgtimes.ru/games/genres/survive/#gb_top')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    plays = html.find_all(class_ = "title")
    play = random.choice(plays)
    play_text2 = play.text
    bot.send_message(message.chat.id,play_text2)
def set_horror(message):
    response = requests.get('https://vgtimes.ru/games/genres/survival-horror/#gb_top')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    plays = html.find_all(class_ = "title")
    play = random.choice(plays)
    play_text3 = play.text
    bot.send_message(message.chat.id,play_text3)
def set_royal(message):
    response = requests.get('https://vgtimes.ru/games/genres/battle-royale/#gb_top')
    response = response.content
    html = BeautifulSoup(response, 'html.parser')
    plays = html.find_all(class_ = "title")
    play = random.choice(plays)
    play_text4 = play.text
    bot.send_message(message.chat.id,play_text4)
@bot.message_handler(content_types = ['text'])
def answer(message):
    if message.text.strip()== 'Факт':
        send_fact(message)
    elif message.text.strip() == 'Стих':
        send_poem(message)
    elif message.text.strip() == 'Стикер':
        send_sticker(message)
    elif message.text.strip() == 'Игра':
        send_play(message)
    elif message.text.strip() == 'Мотивация на каждый день':
        send_motiv(message)
    elif message.text.strip()== 'Экшен':
        set_ekshen(message)
    elif message.text.strip()== 'Выживание':
        set_survive(message)
    elif message.text.strip()== 'Королевская битва':
        set_royal(message)
    elif message.text.strip() == 'Страшное выживание':
        set_horror(message)
bot.polling()