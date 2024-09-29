from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = '7061860896:AAE2vD3un4yFB-ntJD_ox2XcdmnzzM6JgWk'
ADMIN_ID = '5599004374'  # Ensure this is your actual chat ID
user_ids = set()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    print(f"User ID: {user_id}")  # Check the user ID
    user_ids.add(user_id)
    await update.message.reply_text('WELCOME TO DANGER VIP BOT SERVER')

async def send_broadcast_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.chat.id
    if str(user_id) == ADMIN_ID:  # Ensure both are strings
        message = " ".join(context.args)
        for uid in user_ids:
            await context.bot.send_message(chat_id=uid, text=message)
        await update.message.reply_text("Broad cast message sent successful")
    else:
        await update.message.reply_text("You are not authorized for this cammand 🤝✅")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('broadcast', send_broadcast_message))

    app.run_polling()

if __name__ == "__main__":
    main()
# CODES BY DANGER VIP