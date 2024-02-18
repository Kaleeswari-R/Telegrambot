from typing import Final

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '6916487901:AAHeUE15zL5XLRIwZVURyZ7KwGRXAGrPzd0'
BOT_USERNAME: Final = '@aaagribot'


async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello!! I'm agribot")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm here to assist you, tell me something")


async def custom_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Custom command executed")


def handle_response(text: str) -> str:
    process: str = text.lower()

    if 'hello' in process:
        return "Hey there!"
    if 'how are you' in process:
        return 'I am okay, ready to assist you'
    return "I do not understand"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: StopIteration = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, _context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error')


if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_cmd))
    app.add_handler(CommandHandler('help', help_cmd))
    app.add_handler(CommandHandler('custom', custom_cmd))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    print("Polling")
    app.run_polling(poll_interval=3)
