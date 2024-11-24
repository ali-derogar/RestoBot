from config import telegram_bot_api_token
import datetime
import telebot
from src.buttens import *
from src.functions import *
from src.extra import *
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

API_TOKEN = telegram_bot_api_token

current_date = datetime.date.today()
last_try = {}
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    send_welcome_image(bot=bot, message=message)
    start_time(bot=bot, message=message, after_start_markup=after_start_markup)

user_data = {}
user_state = {}

@bot.message_handler(func=lambda message: True)
def keyboard_button_checker(message):
    if message.text == "رزرو":
        reserve = ReservationBot(bot=bot)
        reserve.start(message=message)

    elif message.text == "آدرس":
        address(bot=bot, message=message)

    elif message.text == "تصاویر":
        photos(bot=bot, message=message)

    elif message.text == "گردونه شانس":
        chance(bot, message, last_try, current_date, get_data("foods"))

    elif message.text == "ارتباط با ما":
        contact_us(bot=bot, message=message)

    elif message.text == "منو":
        bot.send_message(message.chat.id, "🍽️ کاوش در انواع طعم‌ها و تجربیات خوراکی! لطفا از منوی زیر برای کشف گزینه‌های ما انتخاب نمایید:", reply_markup=menu_markup)

    elif message.text == "انتقادات و پیشنهادات":
        bot.send_message(message.chat.id, "📬 دیدگاه‌های شما پلی به سوی بهبود ماست. لطفا با استفاده از دکمه‌های زیر، انتقاد یا پیشنهاد خود را با ما در میان بگذارید:", reply_markup=suggestion_markup)

@bot.callback_query_handler(func=lambda call: True)
def handle_query(call):
    sss = SendConversation(bot=bot)
    menus_instance = Menus(bot)
    if call.data == "traditional_foods":
        menus_instance.show_traditional_foods(call.message.chat.id)
    elif call.data == "hookahs":
        menus_instance.show_hookahs(call.message.chat.id)
    elif call.data == "desserts":
        menus_instance.show_desserts(call.message.chat.id)
    elif call.data == "tea":
        menus_instance.show_tea(call.message.chat.id)
    elif call.data == "suggestion" or call.data == "criticism":
        sss.prompt_for_feedback(call.message.chat.id)

def main():
    try:
        bot.infinity_polling()
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
