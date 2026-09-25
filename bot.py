import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

# إعداد السجلات (Logging)
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

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
        text = "💳 **تعبئة الرصيد:**\nالرجاء التحويل إلى حساب شام كاش رقم: `0912345678`\nثم اضغط على الزر أدناه لإرسال رقم العملية أو الإيصال."
        keyboard = [
            [InlineKeyboardButton("📤 إرسال إيصال التحويل", callback_data="send_receipt")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "sham_cash":
        text = "💰 **خدمات شام كاش:**\nاختر نوع الخدمة أو أرسل مبلغ التحويل إلى الحساب المعتمد، ثم تواصل معنا بالإيصال."
        keyboard = [
            [InlineKeyboardButton("📤 إرسال إيصال التحويل", callback_data="send_receipt")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "echancy":
        text = "📊 **قسم الإيتشانسي:**\nخدمات مخصصة وسريعة. يرجى اختيار الخدمة المطلوبة أو التواصل مع الدعم للتفاصيل."
        keyboard = [
            [InlineKeyboardButton("🎧 التواصل مع الدعم", callback_data="support")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "games":
        text = "🎮 **قسم الألعاب:**\nيتوفر لدينا شحن لكافة الألعاب الشهيرة بأسعار منافسة وبسرعة تنفيذ عالية."
        keyboard = [
            [InlineKeyboardButton("💳 اطلب شحن رصيد لعبة", callback_data="recharge")],
            [InlineKeyboardButton("🔙 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard))

    elif data == "main_menu":
        await start(update, context)

    elif data == "send_receipt":
        context.user_data['waiting_for_receipt'] = True
        text = "📥 يرجى إرسال **رقم العملية (Transaction ID)** أو **صورة الإيصال (Screenshot)** الآن في هذه المحادثة وسيتم تحويله للمشرفين فوراً."
        keyboard = [[InlineKeyboardButton("🔙 إلغاء والعودة", callback_data="main_menu")]]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

# استقبال الإيصالات أو الرسائل النصية من المستخدمين
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('waiting_for_receipt'):
        user = update.effective_user
        context.user_data['waiting_for_receipt'] = False
        
        confirmation_text = "✅ تم استلام طلبك وإرسال الإيصال إلى الإدارة بنجاح! سيتم مراجعته وشحن حسابك في أقرب وقت."
        await update.message.reply_text(confirmation_text)
        
        # إذا قمت بوضع الأيدي الخاص بك، سيصلك إشعار بالطلب هنا (اختياري)
        if ADMIN_CHAT_ID != "ضع_معرف_حسابك_هنا":
            forward_msg = f"🔔 طلب دفع جديد من المستخدم:\nالاسم: {user.first_name}\nالمعرف: @{user.username or 'لا يوجد'}\nالايدي: {user.id}"
            try:
                await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=forward_msg)
                await update.message.forward(chat_id=ADMIN_CHAT_ID)
            except Exception as e:
                logger.error(f"Failed to notify admin: {e}")
    else:
        # رد آلي لأي رسالة عشوائية تفتح القائمة
        await start(update, context)

# ----------------- التشغيل الأساسي -----------------
def main():
    keep_alive() # تشغيل السيرفر الوهمي
    
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button_handler))
    application.add_handler(MessageHandler(filters.ALL & ~filters.COMMAND, handle_message))

    print("Bot is up and running...")
    application.run_polling()

if __name__ == "__main__":
    main()
