import os
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'telegrambot_project.settings'
django.setup()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from api.models import User
from asgiref.sync import sync_to_async

API_KEY = 'YOUR-TELEGRAMBOT-API'  # Replace with your actual token


@sync_to_async
def save_telegram_user(tg_user):
    username = tg_user.username if tg_user.username else "username not found"
    return User.objects.update_or_create(
        telegram_id=tg_user.id,
        defaults={
            'username': username,
            'first_name': tg_user.first_name,
            'last_name': tg_user.last_name,
            'is_bot': tg_user.is_bot,
            'language_code': tg_user.language_code,
        }
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tg_user = update.effective_user
    user, created = await save_telegram_user(tg_user)

    firstname = tg_user.first_name
    if created:
        await update.message.reply_text(f" Hello 👋  {firstname}! You've been registered.")
    else:
        await update.message.reply_text(f"Welcome back {firstname}!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Sorry I cannot reply to You 😔 ")


if __name__ == "__main__":
    app = ApplicationBuilder().token(API_KEY).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("✅ Bot is running...")
    app.run_polling()
