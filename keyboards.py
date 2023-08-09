from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def generate_start_button():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button = KeyboardButton(text='Wikipedia')
    markup.add(button)
    return markup