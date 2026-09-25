import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

# إعداد السجلات (Logging)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(name)

# توكن البوت
TOKEN = "8758104476:AAELYEZecA4x78f5ytIZrKctHqEZS7e6sRg"
ADMIN_CHAT_ID = "ضع_معرف_حسابك_هنا" # ضع ايدي حسابك التليجرام هنا لاستلام إشعارات الدفع (اختياري)

# ----------------- خادم Flask للحفاظ على عمل البوت على Render -----------------
app_flask = Flask('')

@app_flask.route('/')
def home():
    return "Bot is active and running!"

def run_flask():
    app_flask.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# ----------------- وظائف وأزرار البوت -----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"أهلاً بك يا {user.first_name} في بوت الخدمات الموثوق ⚡\n\n"
        "اختر الخدمة التي تحتاجها من القائمة أدناه، وسيتولى البوت الباقي.\n"
        "ننتظر منك تجربة مميزة! ❤️"
    )
    
    keyboard = [
        [InlineKeyboardButton("🎮 الألعاب / GAMES", callback_data="games")],
        [InlineKeyboardButton("💳 تعبئة الرصيد / RECHARGE", callback_data="recharge")],
        [InlineKeyboardButton("💰 خدمات شام كاش / SHAM CASH", callback_data="sham_cash")],
        [InlineKeyboardButton("📊 قسم الإيتشانسي / eCHANCY", callback_data="echancy")],
        [InlineKeyboardButton("🎧 خدمة العملاء / SUPPORT TEAM", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.edit_text(welcome_text, reply_markup=reply_markup)

# معالجة الضغط على الأزرار
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "support":
        text = "💬 للاتصال بفريق الدعم الفني، يرجى التواصل عبر المعرف التالي:\n@YourSupportUsername"
        keyboard = [[InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "recharge":
        text = "💳 تعبئة الرصيد:\nالرجاء التحويل إلى حساب شام كاش رقم: 0912345678\nثم اضغط على الزر أدناه لإرسال رقم العملية أو الإيصال."
        keyboard = [
            [InlineKeyboardButton("📤 إرسال إيصال التحويل", callback_data="send_receipt")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "sham_cash":
        text = "💰 خدمات شام كاش:\nاختر نوع الخدمة أو أرسل مبلغ التحويل إلى الحساب المعتمد، ثم تواصل معنا بالإيصال."
        keyboard = [
            [InlineKeyboardButton("📤 إرسال إيصال التحويل", callback_data="send_receipt")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "echancy":
        text = "📊 قسم الإيتشانسي:\nخدمات مخصصة وسريعة. يرجى اختيار الخدمة المطلوبة أو التواصل مع الدعم للتفاصيل."
        keyboard = [
            [InlineKeyboardButton("🎧 التواصل مع الدعم", callback_data="support")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))
