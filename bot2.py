from telegram.ext import Application, Updater, CommandHandler, MessageHandler, filters, CallbackContext
import telegram
from telegram import Update 
import logging
TOKEN = '1193023091:AAEl9eLOZ6Q0PdDRXF07TprHDXt9tEGuclo'
chat_id = 1213182814
bot = telegram.Bot(TOKEN)
print(bot.get_me())
{'id': 514487748, 'first_name': 'trial1', 'is_bot': True, 'username': 'trial3700_bot'}
link='https://bitcoin.org/img/icons/opengraph.png'
bot = telegram.Bot(TOKEN)
def tasveer(name,caption):
  bot.send_photo(chat_id=chat_id, photo=open(name, 'rb'))
  bot.send_message(chat_id=chat_id, text="Alert! Motion detected in Room! "+caption)
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("I'm a bot, Nice to meet you!obey")
def status(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Room status: Unoccupied")  
def convert_uppercase(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text.upper())
def send_image(bot,update,link):
  bot.send_photo(link)
def main():
    # Set up logging
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # Create the Application and pass it your bot's token.
    application = Application.builder().token(TOKEN).build()
    print("Bot started")

    # Add command handlers to the application
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('status', status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, convert_uppercase))

    # Start the Bot
    application.run_polling()
if __name__ == '__main__':
    main()