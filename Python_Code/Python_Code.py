import logging
import serial
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext


com = ""
Arduino_Serial = serial.Serial(com,9600)  


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Select /on to ON LED and /off to OFF LED')


def on(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('LED ON')
    Arduino_Serial.write(str.encode('1'))
    
def off(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('LED OFF')
    Arduino_Serial.write(str.encode('0'))  


def no(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Select /on to ON LED and /off to OFF LED')


def main():

    updater = Updater("TOKEN", use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("on", on))
    dispatcher.add_handler(CommandHandler("off", off))
    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, no))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
