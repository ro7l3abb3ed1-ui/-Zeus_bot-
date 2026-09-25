import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, CallbackQueryHandler, MessageHandler, filters

# إعداد السجلات لمعرفة الأخطاء وحالة التشغيل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = "8758104476:AAELYEZecA4x78f5ytIZrKctHqEZS7e6sRg"

# ----------------- لوحات المفاتيح (Keyboards) -----------------

def main_menu_keyboard():
    keyboard = [
        [InlineKeyboardButton("🎮 الألعاب / GAMES", callback_data="menu_games")],
        [InlineKeyboardButton("💬 التطبيقات الصوتية والدردشة / CHAT APP", callback_data="menu_chat_apps")],
        [InlineKeyboardButton("💳 تعبئة الرصيد / RECHARGE", callback_data="menu_recharge")],
        [InlineKeyboardButton("💰 خدمات شام كاش / SHAM CASH", callback_data="menu_sham_cash")],
        [InlineKeyboardButton("💱 قسم الإيتشانسي / eCHANCY", callback_data="menu_echancy")],
        [InlineKeyboardButton("🔐 توثيق الحسابات / ACCOUNTS VERIFICATION", callback_data="menu_verification")],
        [InlineKeyboardButton("🌐 خدمات متنوعة / Various Services", callback_data="menu_various")],
        [InlineKeyboardButton("🛡️ خدمة تخطي الموقع VPN (بروكسي)", callback_data="menu_vpn")],
        [InlineKeyboardButton("🪟 خدمات ويندوز / WINDOWS SERVICES", callback_data="menu_windows")],
        [InlineKeyboardButton("🌐 خدمات مزودين الانترنت / INTERNET SERVICES", callback_data="menu_internet")],
        [InlineKeyboardButton("🎧 خدمة العملاء / SUPPORT TEAM", callback_data="support")]
    ]
    return InlineKeyboardMarkup(keyboard)

def back_to_main_keyboard():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]])

# ----------------- دوال العرض والتحكم -----------------

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🎉 أهلاً وسهلاً فيك بـ بوت الخدمات الشامل 🤖✨\n\n"
        "🚀 كل خدماتك بمكان واحد وبخطوات سريعة وسهلة!\n"
        "🎮 شحن الألعاب والتطبيقات 💳 شحن الرصيد 🧾 دفع الفواتير 💰 خدمات شام كاش 💱 قسم الإيتشانسي 📲 وخدمات إلكترونية متنوعة تلبي احتياجاتك\n\n"
        "⚡ سرعة في التنفيذ 🔒 خدمة موثوقة 💬 دعم ومتابعة عند الحاجة\n\n"
        "👇 اختر الخدمة اللي بتحتاجها من القائمة وخلّي البوت يهتم بالباقي.\n"
        "❤️ شكراً لثقتك فينا، ونتمنى لك تجربة مميزة!"
    )
    if update.message:
        await update.message.reply_text(welcome_text, reply_markup=main_menu_keyboard())
    elif update.callback_query:
        query = update.callback_query
        await query.answer()
        await query.edit_message_text(text=welcome_text, reply_markup=main_menu_keyboard())

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "main_menu":
        await start(update, context)
        return

    # --- 1. قسم الألعاب ---
    elif data == "menu_games":
        keyboard = [
            [InlineKeyboardButton("Free Fire", callback_data="game_freefire"), InlineKeyboardButton("Jawaker", callback_data="game_jawaker")],
            [InlineKeyboardButton("Global Pubg Mobile", callback_data="game_pubg"), InlineKeyboardButton("Fort Nite", callback_data="game_fortnite")],
            [InlineKeyboardButton("Clash of clans", callback_data="game_coc"), InlineKeyboardButton("Clash royal", callback_data="game_cr")],
            [InlineKeyboardButton("Call of duty", callback_data="game_cod"), InlineKeyboardButton("Delta Force", callback_data="game_delta")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🎮 قسم الألعاب: اختر اللعبة المطلوبة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif data == "game_freefire":
        keyboard = [
            [InlineKeyboardButton("شحن جواهر فري فاير", callback_data="ff_diamonds")],
            [InlineKeyboardButton("عضوية فري فاير", callback_data="ff_membership")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🔥 Free Fire: اختر القسم:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "ff_diamonds":
        keyboard = [
            [InlineKeyboardButton("100 جوهرة - 2$", callback_data="buy_done"), InlineKeyboardButton("210 جوهرة - 3$", callback_data="buy_done")],
            [InlineKeyboardButton("530 جوهرة - 6$", callback_data="buy_done"), InlineKeyboardButton("1080 جوهرة - 12$", callback_data="buy_done")],
            [InlineKeyboardButton("2200 جوهرة - 21.5$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💎 شحن جواهر فري فاير: اختر الباقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "ff_membership":
        keyboard = [
            [InlineKeyboardButton("عضوية اسبوعية - 3$", callback_data="buy_done")],
            [InlineKeyboardButton("عضوية شهرية - 11.5$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("👑 عضوية فري فاير:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "game_jawaker":
        keyboard = [
            [InlineKeyboardButton("10000 توكنز - 1.7$", callback_data="buy_done"), InlineKeyboardButton("10500 توكنز - 1.9$", callback_data="buy_done")],
            [InlineKeyboardButton("11000 توكنز - 2$", callback_data="buy_done"), InlineKeyboardButton("11500 توكنز - 2.3$", callback_data="buy_done")],
            [InlineKeyboardButton("12000 توكنز - 2.5$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🃏 Jawaker: اختر الباقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "game_pubg":
        keyboard = [
            [InlineKeyboardButton("شحن شدات", callback_data="pubg_uc")],
            [InlineKeyboardButton("عضوية Pubg", callback_data="pubg_membership")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🎯 Global Pubg Mobile:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "pubg_uc":
        keyboard = [
            [InlineKeyboardButton("60 شدة - 1.5$", callback_data="buy_done"), InlineKeyboardButton("325 شدة - 5.5$", callback_data="buy_done")],
            [InlineKeyboardButton("660 شدة - 11$", callback_data="buy_done"), InlineKeyboardButton("1800 شدة - 25$", callback_data="buy_done")],
            [InlineKeyboardButton("3850 شدة - 48$", callback_data="buy_done"), InlineKeyboardButton("8100 شدة - 90$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🛒 شحن شدات ببجي:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "pubg_membership":
        keyboard = [
            [InlineKeyboardButton("حزمة الشراء - 1.5$", callback_data="buy_done")],
            [InlineKeyboardButton("حزمة ترقية الاسلحة - 4$", callback_data="buy_done")],
            [InlineKeyboardButton("حزمة الشعار الخرافي - 5.5$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("📦 عضويات وباقات ببجي:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif data in ["game_coc", "game_cr"]:
        await query.edit_message_text("⏳ قريباً...", reply_markup=back_to_main_keyboard(), parse_mode="Markdown")

    elif data == "game_delta":
        keyboard = [
            [InlineKeyboardButton("320 كوينز - 5$", callback_data="buy_done"), InlineKeyboardButton("460 كوينز - 7$", callback_data="buy_done")],
            [InlineKeyboardButton("750 كوينز - 9$", callback_data="buy_done"), InlineKeyboardButton("1480 كوينز - 17.5$", callback_data="buy_done")],
            [InlineKeyboardButton("1980 كوينز - 21.5$", callback_data="buy_done"), InlineKeyboardButton("3950 كوينز - 43$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🛡️ Delta Force: اختر الباقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "game_cod":
        keyboard = [
            [InlineKeyboardButton("420 cp - 7.5$", callback_data="buy_done"), InlineKeyboardButton("880 cp - 14$", callback_data="buy_done")],
            [InlineKeyboardButton("2400 cp - 25$", callback_data="buy_done"), InlineKeyboardButton("5000 cp - 68$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🎖️ Call of Duty: اختر الباقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "game_fortnite":
        keyboard = [
            [InlineKeyboardButton("بطاقة 2800 - 33$", callback_data="buy_done")],
            [InlineKeyboardButton("بطاقة 5000 - 53$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("⚡ Fortnite: اختر البطاقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # --- 2. التطبيقات الصوتية والدردشة ---
    elif data == "menu_chat_apps":
        keyboard = [
            [InlineKeyboardButton("Bigo Live", callback_data="app_bigo"), InlineKeyboardButton("Soul Chill", callback_data="app_soulchill")],
            [InlineKeyboardButton("Likee Live", callback_data="app_likee"), InlineKeyboardButton("Zaffa Live", callback_data="app_zaffa")],
            [InlineKeyboardButton("Sugo Chat", callback_data="app_sugo"), InlineKeyboardButton("Honey Jar", callback_data="app_honeyjar")],
            [InlineKeyboardButton("Soul Chat", callback_data="app_soulchat"), InlineKeyboardButton("Mico Live", callback_data="app_mico")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💬 التطبيقات الصوتية والدردشة: اختر التطبيق:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_bigo":
        keyboard = [
            [InlineKeyboardButton("50 - 1.5$", callback_data="buy_done"), InlineKeyboardButton("75 - 1.75$", callback_data="buy_done")],
            [InlineKeyboardButton("100 - 2.5$", callback_data="buy_done"), InlineKeyboardButton("125 - 2.75$", callback_data="buy_done")],
            [InlineKeyboardButton("150 - 3.25$", callback_data="buy_done"), InlineKeyboardButton("175 - 3.75$", callback_data="buy_done")],
            [InlineKeyboardButton("200 - 4.25$", callback_data="buy_done"), InlineKeyboardButton("225 - 4.75$", callback_data="buy_done")],
            [InlineKeyboardButton("250 - 5$", callback_data="buy_done"), InlineKeyboardButton("350 - 7$", callback_data="buy_done")],
            [InlineKeyboardButton("450 - 9$", callback_data="buy_done"), InlineKeyboardButton("550 - 11$", callback_data="buy_done")],
            [InlineKeyboardButton("650 - 13$", callback_data="buy_done"), InlineKeyboardButton("850 - 17$", callback_data="buy_done")],
            [InlineKeyboardButton("1000 - 20$", callback_data="buy_done"), InlineKeyboardButton("1500 - 30$", callback_data="buy_done")],
            [InlineKeyboardButton("2000 - 38.5$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🟠 Bigo Live:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_soulchill":
        keyboard = [
            [InlineKeyboardButton("1000 كريستالة - 2.5$", callback_data="buy_done"), InlineKeyboardButton("1500 كريستالة - 3$", callback_data="buy_done")],
            [InlineKeyboardButton("2000 كريستالة - 4$", callback_data="buy_done"), InlineKeyboardButton("2500 كريستالة - 5$", callback_data="buy_done")],
            [InlineKeyboardButton("3000 كريستالة - 6$", callback_data="buy_done"), InlineKeyboardButton("3500 كريستالة - 7$", callback_data="buy_done")],
            [InlineKeyboardButton("4000 كريستالة - 8$", callback_data="buy_done"), InlineKeyboardButton("5000 كريستالة - 10$", callback_data="buy_done")],
            [InlineKeyboardButton("6000 كريستالة - 11$", callback_data="buy_done"), InlineKeyboardButton("7000 كريستالة - 14$", callback_data="buy_done")],
            [InlineKeyboardButton("10000 كريستالة - 20$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🔵 Soul Chill:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_likee":
        keyboard = [
            [InlineKeyboardButton("100 - 3$", callback_data="buy_done"), InlineKeyboardButton("200 - 5$", callback_data="buy_done")],
            [InlineKeyboardButton("300 - 7$", callback_data="buy_done"), InlineKeyboardButton("400 - 9$", callback_data="buy_done")],
            [InlineKeyboardButton("500 - 11$", callback_data="buy_done"), InlineKeyboardButton("1000 - 20$", callback_data="buy_done")],
            [InlineKeyboardButton("1500 - 30$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💙 Likee Live:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_zaffa":
        keyboard = [
            [InlineKeyboardButton("60000 - 2$", callback_data="buy_done"), InlineKeyboardButton("70000 - 2.5$", callback_data="buy_done")],
            [InlineKeyboardButton("80000 - 3$", callback_data="buy_done"), InlineKeyboardButton("90000 - 3.5$", callback_data="buy_done")],
            [InlineKeyboardButton("100000 - 4$", callback_data="buy_done"), InlineKeyboardButton("500000 - 9$", callback_data="buy_done")],
            [InlineKeyboardButton("1000000 - 17$", callback_data="buy_done"), InlineKeyboardButton("2000000 - 33$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🟣 Zaffa Live:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_sugo":
        keyboard = [
            [InlineKeyboardButton("10000 - 2$", callback_data="buy_done"), InlineKeyboardButton("20000 - 3.5$", callback_data="buy_done")],
            [InlineKeyboardButton("30000 - 5.5$", callback_data="buy_done"), InlineKeyboardButton("40000 - 6.5$", callback_data="buy_done")],
            [InlineKeyboardButton("50000 - 8.5$", callback_data="buy_done"), InlineKeyboardButton("100000 - 16$", callback_data="buy_done")],
            [InlineKeyboardButton("500000 - 76$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🟡 Sugo Chat:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif data == "app_honeyjar":
        keyboard = [
            [InlineKeyboardButton("1000 - 10$", callback_data="buy_done"), InlineKeyboardButton("2000 - 18$", callback_data="buy_done")],
            [InlineKeyboardButton("3000 - 26$", callback_data="buy_done"), InlineKeyboardButton("4000 - 33$", callback_data="buy_done")],
            [InlineKeyboardButton("5000 - 43$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🍯 Honey Jar:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_soulchat":
        keyboard = [
            [InlineKeyboardButton("10000 - 2.5$", callback_data="buy_done"), InlineKeyboardButton("20000 - 3.5$", callback_data="buy_done")],
            [InlineKeyboardButton("30000 - 5.5$", callback_data="buy_done"), InlineKeyboardButton("40000 - 7.5$", callback_data="buy_done")],
            [InlineKeyboardButton("50000 - 8.5$", callback_data="buy_done"), InlineKeyboardButton("100000 - 16.5$", callback_data="buy_done")],
            [InlineKeyboardButton("500000 - 78$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🔹 Soul Chat:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "app_mico":
        keyboard = [
            [InlineKeyboardButton("5000 - 4$", callback_data="buy_done"), InlineKeyboardButton("10000 - 7$", callback_data="buy_done")],
            [InlineKeyboardButton("20000 - 10$", callback_data="buy_done"), InlineKeyboardButton("30000 - 13$", callback_data="buy_done")],
            [InlineKeyboardButton("40000 - 17$", callback_data="buy_done"), InlineKeyboardButton("50000 - 20$", callback_data="buy_done")],
            [InlineKeyboardButton("100000 - 35$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🟢 Mico Live:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # --- 3. تعبئة الرصيد (RECHARGE) ---
    elif data == "menu_recharge":
        keyboard = [
            [InlineKeyboardButton("Syriatel", callback_data="recharge_syriatel"), InlineKeyboardButton("MTN", callback_data="recharge_mtn")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💳 تعبئة الرصيد (RECHARGE):", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data in ["recharge_syriatel", "recharge_mtn"]:
        context.user_data['waiting_input'] = "recharge"
        await query.edit_message_text(
            "📦 الخدمة: تعبئة رصيد\n✍️ يرجى تزويدنا بالمعلومات المطلوبة (الرقم، كود التعبئة، أو تفاصيل الاشتراك) في رسالة واحدة:",
            reply_markup=back_to_main_keyboard()
        )

    # --- 4. توثيق الحسابات ---
    elif data == "menu_verification":
        keyboard = [
            [InlineKeyboardButton("توثيق حساب يوتيوب", callback_data="ver_youtube")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🔐 توثيق الحسابات: اختر المنصة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "ver_youtube":
        keyboard = [
            [InlineKeyboardButton("1 شهر - 4.5$", callback_data="buy_done"), InlineKeyboardButton("3 شهر - 12$", callback_data="buy_done")],
            [InlineKeyboardButton("6 شهر - 21$", callback_data="buy_done"), InlineKeyboardButton("12 شهر - 35$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("📺 توثيق يوتيوب: اختر المدة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    # --- 5. خدمات متنوعة ---
    elif data == "menu_various":
        keyboard = [
            [InlineKeyboardButton("نجوم تلغرام", callback_data="var_telegram_stars")],
            [InlineKeyboardButton("الرد التلقائي للفيسبوك", callback_data="var_fb_auto")],
            [InlineKeyboardButton("تطبيق الارقام", callback_data="var_numbers")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🌐 خدمات متنوعة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "var_telegram_stars":
        keyboard = [
            [InlineKeyboardButton("50 نجمة - 2$", callback_data="buy_done"), InlineKeyboardButton("100 نجمة - 3$", callback_data="buy_done")],
            [InlineKeyboardButton("500 نجمة - 11$", callback_data="buy_done"), InlineKeyboardButton("1000 نجمة - 21$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("⭐ نجوم تلغرام:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "var_fb_auto":
        keyboard = [
            [InlineKeyboardButton("1 شهر - 5$", callback_data="buy_done"), InlineKeyboardButton("3 شهر - 10$", callback_data="buy_done")],
            [InlineKeyboardButton("6 شهر - 20$", callback_data="buy_done"), InlineKeyboardButton("12 شهر - 30$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🤖 الرد التلقائي للفيسبوك:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "var_numbers":
        context.user_data['waiting_input'] = "numbers"
        await query.edit_message_text(
            "📲 تطبيق الارقام\n✍️ يرجى تزويدنا بالتفاصيل المطلوبة في رسالة واحدة:",
            reply_markup=back_to_main_keyboard()
        )

    # --- 6. خدمة تخطي الموقع VPN (بروكسي) ---
    elif data == "menu_vpn":
        keyboard = [
            [InlineKeyboardButton("Express VPN", callback_data="vpn_express")],
            [InlineKeyboardButton("Hotspot Shield", callback_data="vpn_hotspot")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🛡️ خدمة تخطي الموقع VPN:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "vpn_express":
        keyboard = [
            [InlineKeyboardButton("تفعيل للكمبيوتر 1 شهر - 20$", callback_data="buy_done")],
            [InlineKeyboardButton("تفعيل للهاتف 1 شهر - 5$", callback_data="buy_done")],
            [InlineKeyboardButton("تفعيل للهاتف 3 شهر - 13$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🚀 Express VPN:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "vpn_hotspot":
        keyboard = [
            [InlineKeyboardButton("اشتراك 1 شهر - 2$", callback_data="buy_done"), InlineKeyboardButton("اشتراك 3 شهر - 3$", callback_data="buy_done")],
            [InlineKeyboardButton("اشتراك 6 شهر - 4$", callback_data="buy_done"), InlineKeyboardButton("اشتراك 12 شهر - 6$", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🛡️ Hotspot Shield:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # --- 7. خدمات ويندوز ---
    elif data == "menu_windows":
        context.user_data['waiting_input'] = "windows"
        await query.edit_message_text(
            "🪟 خدمات ويندوز\n✍️ يرجى تزويدنا بالمعلومات المطلوبة في رسالة واحدة:",
            reply_markup=back_to_main_keyboard()
        )
        
    # --- 8. خدمات مزودين الانترنت ---
    elif data == "menu_internet":
        keyboard = [
            [InlineKeyboardButton("مزود سوا", callback_data="net_provider")],
            [InlineKeyboardButton("مزود رن نت", callback_data="net_provider")],
            [InlineKeyboardButton("مزود أية", callback_data="net_provider")],
            [InlineKeyboardButton("مزود تكامل", callback_data="net_provider")],
            [InlineKeyboardButton("الجمعية العلمية السورية للمعلوماتية", callback_data="net_provider")],
            [InlineKeyboardButton("مزود السورية للاتصالات", callback_data="net_provider")],
            [InlineKeyboardButton("مزود أمواج", callback_data="net_provider")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🌐 خدمات مزودين الانترنت: اختر المزود:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "net_provider":
        context.user_data['waiting_input'] = "internet"
        await query.edit_message_text(
            "🌐 مزود الانترنت\n📞 الرجاء تزويدنا بالرقم الأرضي مع مفتاح المحافظة:",
            reply_markup=back_to_main_keyboard()
        )

    # --- 9. خدمات شام كاش ---
    elif data == "menu_sham_cash":
        keyboard = [
            [InlineKeyboardButton("شحن رصيد", callback_data="sham_deposit")],
            [InlineKeyboardButton("سحب رصيد", callback_data="sham_withdraw")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💰 خدمات شام كاش (SHAM CASH):", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data in ["sham_deposit", "sham_withdraw"]:
        action_name = "شحن رصيد شام كاش" if data == "sham_deposit" else "سحب رصيد شام كاش"
        context.user_data['waiting_input'] = "sham"
        await query.edit_message_text(
            f"💰 {action_name}\n✍️ يرجى تزويدنا بالمعلومات المطلوبة (المبلغ، الحساب، التفاصيل) في رسالة واحدة:",
            reply_markup=back_to_main_keyboard()
        )

    # --- 10. قسم الإيتشانسي eCHANCY ---
    elif data == "menu_echancy":
        keyboard = [
            [InlineKeyboardButton("ichancy (سحب/شحن)", callback_data="echancy_main")],
            [InlineKeyboardButton("شحن رصيد في البوت", callback_data="echancy_deposit_bot")],
            [InlineKeyboardButton("سحب رصيد من البوت", callback_data="echancy_withdraw_bot")],
            [InlineKeyboardButton("رسالة للدعم", callback_data="support")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💱 قسم الإيتشانسي (eCHANCY):", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "echancy_main":
        keyboard = [
            [InlineKeyboardButton("حذف الحساب", callback_data="buy_done"), InlineKeyboardButton("شحن الحساب", callback_data="buy_done")],
            [InlineKeyboardButton("شحن كامل الرصيد", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("🎰 خدمات ichancy:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    elif data == "echancy_deposit_bot":
        keyboard = [
            [InlineKeyboardButton("Sham cash (usd-syp)", callback_data="buy_done")],
            [InlineKeyboardButton("Syriatel cash", callback_data="buy_done")],
            [InlineKeyboardButton("Binance", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💳 شحن رصيد في البوت (eCHANCY): اختر الطريقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")
        
    elif data == "echancy_withdraw_bot":
        keyboard = [
            [InlineKeyboardButton("Sham cash (usd-syp)", callback_data="buy_done")],
            [InlineKeyboardButton("Syriatel cash", callback_data="buy_done")],
            [InlineKeyboardButton("Binance", callback_data="buy_done")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")]
        ]
        await query.edit_message_text("💵 سحب رصيد من البوت (eCHANCY): اختر الطريقة:", reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="Markdown")

    # --- الدعم الفني ---
    elif data == "support":
        context.user_data['waiting_input'] = "support"
        await query.edit_message_text(
            "🎧 خدمة العملاء والدعم الفني\n✍️ اكتب رسالتك أو استفسارك وسيتم تحويله للدعم:",
            reply_markup=back_to_main_keyboard()
        )

    # --- إتمام الشراء / الطلب النهائي ---
    elif data == "buy_done":
        await query.edit_message_text(
            "✅ تم استلام طلبك، ستتم المعالجة خلال مدة أقصاها ربع ساعة، شكراً لانتظاركم ❤️",
            reply_markup=back_to_main_keyboard()
        )

# ----------------- معالجة رسائل النصوص المدخلة من المستخدم -----------------
async def handle_text_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    waiting_type = context.user_data.get('waiting_input')
    
    if waiting_type == "internet":
        await update.message.reply_text(
            "✅ سيتم معالجة طلبك خلال فترة أقصاها نصف ساعة. شكراً لتزويدنا بالرقم الأرضي!",
            reply_markup=back_to_main_keyboard()
        )
    elif waiting_type:
        await update.message.reply_text(
            "✅ تم استلام طلبك، ستتم المعالجة خلال مدة أقصاها ربع ساعة، شكراً لانتظاركم ❤️",
            reply_markup=back_to_main_keyboard()
        )
    else:
        await update.message.reply_text(
            "أهلاً بك! يرجى استخدام القائمة الرئيسية لاختيار الخدمة المطلوبة 👇",
            reply_markup=main_menu_keyboard()
        )
    
    # إعادة تعيين الحالة
    context.user_data['waiting_input'] = None

# ----------------- الدالة الرئيسية لتشغيل البوت -----------------
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_messages))

    print("البوت يعمل الآن بنجاح...")
    app.run_polling()

if __name__ == "__main__":
    main()
