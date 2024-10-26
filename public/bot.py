from telegram import Update, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

API_TOKEN = '7706911294:AAG1WL05OBHf3ToCbvA56_j-hzN6ZV5ev9A'  # O'zingizning tokeningizni qo'ying

async def start(update: Update, context):
    user_first_name = update.message.from_user.first_name 
    await update.message.reply_text(
        f"Assalomu alaykum, {user_first_name}! WebApp-ni ochish uchun quyidagi tugmani bosing.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="WebApp-ni ochish", web_app={"url": "https://www.olx.uz/"})]
        ])
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
