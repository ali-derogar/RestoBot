import random 
import datetime
import jdatetime
from src.buttens import *
import os
from .extra import get_multiple_data

def get_date(timestamp):

    gregorian_date = datetime.datetime.utcfromtimestamp(timestamp)

    hijri_date = jdatetime.date.fromgregorian(date=gregorian_date)

    formatted_date = hijri_date.strftime('%Y/%m/%d')
    formatted_time = gregorian_date.strftime('%H:%M')

    return f"{formatted_date} - {formatted_time}"

def address(bot , message):
    latitude = 35.7056636
    longitude = 50.9365807
    bot.send_message(
        message.chat.id , """\
🏠 آدرس:\
 رستوران بیدستان، واقع در فردیس خوشنام، کنار پادگان فتح .\
\n\n\
📍 نقشه را لمس کنید تا به راحتی مسیر خود را پیدا کنید .
"""),
    bot.send_location(message.chat.id, latitude, longitude)

# -----------------------------------------------------------------------------------------------------------------------------


def photos(bot, message):
    photo_path = 'static/photos/'
    for photo_file in os.listdir(photo_path):
        full_path = os.path.join(photo_path, photo_file)
        if os.path.isfile(full_path):
            with open(full_path, 'rb') as photo:
                bot.send_photo(message.chat.id, photo)


# -----------------------------------------------------------------------------------------------------------------------------


def send_welcome_image(bot ,message):
    photo_path = 'static/photos/n_2.jpeg' 
    with open(photo_path, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)

def start_time(bot , message , after_start_markup):
    bot.send_message(message.chat.id,
"""\
```\
\
🎉🍴 خوش آمدید به جشن طعم‌ها در رستوران بیدستان! 🍴🎉\
🕚 از ساعت ١١ صبح تا ١٢ نیمه‌شب، پادشاهی غذاهای لذیذ 😍 و قلیان‌های رویایی منتظر شماست! 🌬️💨\
🎵 وای! فراموش نکنید، موسیقی زنده‌مون هم که دیگه... حرف نداره! 🎶🎷\
🎉 بیایید و در مهمانی ما شرکت کنید، جایی که هر شب، شبی به یادماندنی است! 🥳\
📍 ما رو پیدا کنید در: فردیس خوشنام، جنب پادگان فتح. نقشه ما را دنبال کنید، مثل گنجی در انتظار شما! 🗺️📍\
❤️ بی‌صبرانه منتظر دیدار شما هستیم! بزنید روی دکمه و بیایید توی دنیای خوشمزگی‌ها! 🤩👇\
```
\
""" ,
 reply_markup=after_start_markup)
    

def contact_us(bot , message):

    contact_info = "برای ارتباط با ما، از راه‌های زیر استفاده کنید:\n\n"
    contact_info += "📧 ایمیل: info@example.com\n"
    contact_info += "🌐 وب سایت: www.google.com\n"
    contact_info += "📞 تلفن: 123456789\n"
    contact_info += "📱 تلگرام: @armin1129"
    bot.reply_to(message, contact_info)





def chance(bot , message , last_try , current_date , foods):
    user_id = message.from_user.id
    if user_id not in last_try or last_try[user_id] != current_date:
        last_try[user_id] = current_date 

        bot.send_animation(message.chat.id, animation="https://media1.tenor.com/m/Fnilxre1a3kAAAAd/wheel-of-fortune-wheel.gif")
        prize = random.choice(foods)  # فرض بر اینکه لیست foods تعریف شده است
        discount = random.choice(['10%', '15%', '20%'])
        content = f"وای وای وای! 🎉 {message.from_user.first_name} عزیز، شما چقدر خوش شانسید! 🌟\n\n"
        content += "با هیجان اعلام می‌کنیم که شما برنده‌ی یک تخفیف شگفت‌انگیز شده‌اید! 🥳\n\n"
        content += f"تخفیف {discount} برای {prize}! فقط تصور کنید، همین {prize} خوشمزه با قیمتی باورنکردنی! 😋\n\n"
        content += "می‌توانید از این تخفیف از شنبه تا چهارشنبه استفاده کنید. فراموش نکنید، این فرصت عالی رو از دست ندهید!\n\n"
        content += f"تاریخ اعتبار تخفیف: {get_date(message.date)} 🗓️\n\n"
        content += "منتظر دیدن لبخند رضایت شما هستیم! 😊"

        bot.send_message(message.chat.id, content)
    else:
        bot.send_message(message.chat.id, "شما امروز قبلاً گردونه شانس را چرخانده‌اید. لطفاً فردا دوباره تلاش کنید!")


# ----------------------------------------------------------------------------------------------------------------------------------------------
        

class ReservationBot:

    def __init__(self, bot):
        self.bot = bot
        self.user_data = {}
        self.user_state = {}  # Initialize user_state

    def start(self, message):
        chat_id = message.chat.id
        msg = self.bot.send_message(chat_id, "لطفا تعداد نفرات را وارد کنید:")
        self.bot.register_next_step_handler(msg, self.process_people_count)

    def process_people_count(self, message):
        chat_id = message.chat.id
        username = message.from_user.username
        self.user_data[chat_id] = {'people_count': message.text, 'username': username}
        msg = self.bot.send_message(chat_id, "عالی است! حالا لطفا تاریخ رزرو را به شکل (مثال: 1402/05/12) وارد کنید. مشتاقانه منتظر رزرو شما هستیم! 😊")
        self.bot.register_next_step_handler(msg, self.process_reservation_date)

    def process_reservation_date(self, message):
        chat_id = message.chat.id
        self.user_data[chat_id]['reservation_date'] = message.text
        msg = self.bot.send_message(chat_id, "درخشان! حالا نوبت به وارد کردن نام شما رسیده، لطفا نام خود را وارد کنید:")
        self.bot.register_next_step_handler(msg, self.process_name)

    def process_name(self, message):
        chat_id = message.chat.id
        self.user_data[chat_id]['name'] = message.text
        msg = self.bot.send_message(chat_id, "تقریبا تمام شد! فقط لازم است شماره تماس خود را وارد کنید تا در صورت نیاز بتوانیم با شما تماس بگیریم:")
        self.bot.register_next_step_handler(msg, self.process_contact)

    def process_contact(self, message):
        chat_id = message.chat.id
        self.user_data[chat_id]['contact'] = message.text
        self.send_reservation_details(chat_id)
        self.user_state[chat_id] = 'RESERVATION_COMPLETED'  # تغییر وضعیت

    def send_reservation_details(self, chat_id):
        details = self.user_data[chat_id]
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reservation_info = f"🌟 رزرو جدید ({now}) 🌟\nنام کاربری: @{details['username']}\nتعداد نفرات: {details['people_count']}\nتاریخ رزرو: {details['reservation_date']}\nنام: {details['name']}\nتماس: {details['contact']}\nشناسه کاربر: {chat_id}"
        self.bot.send_message("175774036", reservation_info)  # ارسال اطلاعات به ادمین

        # پیام تایید رزرو به همراه پیام ذخیره‌شدن اطلاعات جذاب‌تر
        confirmation_message = "اطلاعات رزرو شما با موفقیت ارسال و ثبت شد. برای تایید نهایی رزرو با شما تماس خواهیم گرفت. مشتاقانه منتظر دیدار شما هستیم! 🎉"
        self.bot.send_message(chat_id, confirmation_message, reply_markup=confirmation_markup)
        



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        
class Menus():

    def __init__(self, bot):
        self.bot = bot

    def show_traditional_foods(self, chat_id):
        traditional_foods = get_multiple_data("traditional_foods")
        self.bot.send_message(chat_id, traditional_foods, parse_mode='Markdown')

    def show_hookahs(self, chat_id):
        hookahs = get_multiple_data("hookahs")
        self.bot.send_message(chat_id, hookahs, parse_mode='Markdown')


    def show_desserts(self, chat_id):
        desserts = get_multiple_data("desserts")
        self.bot.send_message(chat_id, desserts, parse_mode='Markdown')


    def show_tea(self, chat_id):
        tea = get_multiple_data("tea")
        self.bot.send_message(chat_id, tea, parse_mode='Markdown')



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class SendConversation():
    def __init__(self, bot):
        self.bot = bot

    def prompt_for_feedback(self, chat_id):
        invitation_message = "درود بر شما 🌟، از شما دعوت می‌کنیم تا با اشتراک‌گذاری نظرات و پیشنهادات‌تان، به ما در ارائه خدمات بهتر یاری رسانید. لطفا پیام خود را بنویسید 📝:"
        msg = self.bot.send_message(chat_id, invitation_message)
        self.bot.register_next_step_handler(msg, self.receive_feedback)

    def receive_feedback(self, message):
        chat_id = message.chat.id
        user_feedback = message.text
        self.send_feedback_to_admin(user_feedback, message)
        gratitude_message = "بازخورد شما با ارزش است و با موفقیت ثبت شد 🌈. از وقت و اعتمادی که به ما اختصاص دادید، صمیمانه سپاسگزاریم! 🙏😊"
        self.bot.send_message(chat_id, gratitude_message)

    def send_feedback_to_admin(self, user_feedback, message):
        user_name = message.from_user.username
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        feedback_message = f"📣 بازخورد جدید از @{user_name} ({now}) 📣\nپیشنهاد یا انتقاد: {user_feedback}"
        self.bot.send_message("175774036", feedback_message) 

