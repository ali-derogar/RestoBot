import telebot

after_start_1 = telebot.types.KeyboardButton("رزرو")
after_start_2 = telebot.types.KeyboardButton("آدرس")
after_start_3 = telebot.types.KeyboardButton("ارتباط با ما")
after_start_4 = telebot.types.KeyboardButton("منو")
after_start_5 = telebot.types.KeyboardButton("انتقادات و پیشنهادات")
after_start_6 = telebot.types.KeyboardButton("گردونه شانس")
after_start_7 = telebot.types.KeyboardButton("تصاویر")
after_start_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=3)
after_start_markup.add(after_start_1,after_start_2,after_start_3,after_start_4,after_start_5,after_start_6,after_start_7)

menu_markup = telebot.types.InlineKeyboardMarkup(row_width=2)
menu_button1 = telebot.types.InlineKeyboardButton("💨 قلیان‌ها", callback_data='hookahs')
menu_button2 = telebot.types.InlineKeyboardButton("🍲 غذا‌های سنتی", callback_data='traditional_foods')
menu_button3 = telebot.types.InlineKeyboardButton("🍰 دسرها", callback_data='desserts')
menu_button4 = telebot.types.InlineKeyboardButton("🍵 چای", callback_data='tea')
menu_markup.add(menu_button1, menu_button2, menu_button3, menu_button4)


# ارسال پیام تأیید رزرو به کاربر با استفاده از کیبورد شیک تر
confirmation_markup = telebot.types.InlineKeyboardMarkup(row_width=1)
confirm_button = telebot.types.InlineKeyboardButton("تأیید رزرو", callback_data='confirm_reservation')
confirmation_markup.add(confirm_button)


suggestion_button = telebot.types.InlineKeyboardButton("💡 پیشنهاد دوستانه 💡", callback_data='suggestion')
criticism_button = telebot.types.InlineKeyboardButton("🔍 انتقاد سازنده 🔍", callback_data='criticism')
suggestion_markup = telebot.types.InlineKeyboardMarkup()
suggestion_markup.add(suggestion_button, criticism_button)
