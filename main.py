import confic
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup

from telebot.types import InlineKeyboardButton
from telebot.types import InlineKeyboardMarkup
import cv2

bot = TeleBot(confic.token)
keyboard = ReplyKeyboardMarkup(True)
keyboard.row('/start', '/info')
keyboard.row('Привет', 'Пока')
sticker1 = 'CAACAgIAAxkBAAN7YEJhVKj0vsDNV0JCR53AFfpzDFYAAgEBAAJWnb0KIr6fDrjC5jQeBA'

@bot.message_handler(commands=['start'])
def start(message):
    print(message.chat.id, message.text)
    bot.send_sticker(message.chat.id, sticker1)
    bot.send_message(message.chat.id, "Бот запущен", reply_markup=keyboard)


@bot.message_handler(commands=['info'])
def info(message):
    print(message.chat.id, message.text)
    bot.send_message(message.chat.id, "Это бот Хабибуллина Раяна", reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def lalala(message_text):
    print(message_text.chat.id, message_text.text)
    bot.send_message(message_text.chat.id, 'Принято', reply_markup=keyboard)


@bot.message_handler(content_types=['photo'])
def receive_photo(message_photo):
    photo_id = message_photo.photo[-1].file_id
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("image.jpg", "wb") as new_file:
        new_file.write(downloaded_file)
    new_file.close()
    inline = InlineKeyboardMarkup()
    item1=InlineKeyboardButton(text='Введите размер', callback_data='info')
    inline.add(item1)
    bot.send_message(message_photo.chat.id, '!', reply_markup=inline)
    image = cv2.imread("image.jpg")
    image_resize = cv2.resize(image, (500, 1000))
    cv2.imwrite('image_resize.jpg', image_resize)
    cv2.imshow('w', image_resize)
    cv2.waitKey(1000)
    photo = open('image_resize.jpg', 'rb')
    bot.send_photo(message_photo.chat.id, photo)


# bot.send_message(confic.my_chat_id, "Привет я бот")
bot.polling(none_stop=True)
