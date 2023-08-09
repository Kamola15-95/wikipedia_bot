from telebot import TeleBot
from telebot.types import Message
import wikipedia
from keyboards import generate_start_button

TOKEN = '6178681976:AAGKrPkbG2DvPzL9zXpkpMSdLD2oClVALx4'

bot = TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def command_start(message: Message):
    chat_id = message.chat.id
    text = 'Привет! Для начала поиска информации нажми кнопку ниже.'
    bot.send_message(chat_id, text, reply_markup=generate_start_button())

@bot.message_handler(regexp='Wikipedia')
def reaction_to_wikipedia_button(message: Message):
    chat_id = message.chat.id
    text = 'Введите запрос: '
    bot.send_message(chat_id, text)

@bot.message_handler(func=lambda message: True)
def search_info(message):
    wikipedia.set_lang('ru')
    query = message.text
    try:
        page = wikipedia.page(query)
        summary = wikipedia.summary(query, sentences=6)
        response = f"<b>{page.title}</b>\n\n{summary}\n\n<b>Ссылка:</b> {page.url}"
        bot.send_message(message.chat.id, response, parse_mode='HTML')
    except wikipedia.PageError:
        response = "По вашему запросу ничего не найдено. Попробуйте изменить запрос."
        bot.send_message(message.chat.id, response)

bot.polling(none_stop=True)