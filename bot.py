import logging
import json
import os
import urllib3

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

APP_NAME = 'https://covidnineteentelebot.herokuapp.com/'
PORT = int(os.environ.get('PORT', '8443'))
TOKEN = '1671586129:AAGJgSkfARogaKIMuyTD6-9PCxVkp1IsRPI'
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Data Kasus Covid-19 di ' + str(dataIndo[0]['name']) +'\n' + '\n' + '🤒Positif: ' + str(dataIndo[0]['positif']) + '\n' + '🙂Sembuh: ' + str(dataIndo[0]['sembuh']) + '\n' + "☠Meninggal: " + str(dataIndo[0]['meninggal']) + '\n' + "🛏Dirawat: " + str(dataIndo[0]['dirawat']))


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text('Saya tidak mengerti apa itu ' + '"'+ update.message.text + '"' + '. Maaf, saya akan mempelajari hal itu segera.')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

# Define a few province information that you want to share (ex: confirmed, actives, deaths, ect.)

def nameProv(id):
    """Return province name"""
    return "Provinsi: " + str(dataProv[id]['attributes']['Provinsi'])


def deathProv(id):
    """Return province death case"""
    return "☠Meninggal: " + str(dataProv[id]['attributes']['Kasus_Meni'])


def activeProv(id):
    """Return province active case"""
    return "🤒Positif: " + str(dataProv[id]['attributes']['Kasus_Posi'])


def recoveredProv(id):
    """Return province recovered case"""
    return "🙂Sembuh: " + str(dataProv[id]['attributes']['Kasus_Semb'])

# Define a few command to display covid information per province

def jakarta(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 0
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def jabar(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 1
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def jatim(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 2
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def jateng(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 3
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sulsel(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 4
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kaltim(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 5
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def riau(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 6
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sumbar(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 7
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def banten(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 8
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def bali(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 10
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kalsel(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 11
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def yogyakarta(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 12
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def papua(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 13
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sumsel(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 14
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kalteng(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 15
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sulut(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 16
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def aceh(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 17
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sultenggara(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 18
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kep_riau(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 19
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def lampung(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 20
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def papua_barat(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 21
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def ntb(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 22
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def maluku(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 23
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kalimantan_utara(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 24
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sulteng(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 25
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def bengkulu(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 26
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def gorontalo(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 27
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def jambi(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 28
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def kalbar(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 29
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def maluku_utara(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 30
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def bangka(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 31
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def ntt(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 32
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

def sulbar(update, context):
    """Send a message when the command /jakarta is issued."""
    id = 33
    update.message.reply_text(nameProv(id) + '\n'  + activeProv(id) + '\n' + recoveredProv(id) + '\n' + deathProv(id))

# Main program

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("jakarta", jakarta))
    dp.add_handler(CommandHandler("jabar", jabar))
    dp.add_handler(CommandHandler("jatim", jatim))
    dp.add_handler(CommandHandler("jateng", jateng))
    dp.add_handler(CommandHandler("sulsel", sulsel))
    dp.add_handler(CommandHandler("kaltim", kaltim))
    dp.add_handler(CommandHandler("riau", riau))
    dp.add_handler(CommandHandler("sumbar", sumbar))
    dp.add_handler(CommandHandler("banten", banten))
    dp.add_handler(CommandHandler("bali", bali))
    dp.add_handler(CommandHandler("kalsel", kalsel))
    dp.add_handler(CommandHandler("yogyakarta", yogyakarta))
    dp.add_handler(CommandHandler("papua", papua))
    dp.add_handler(CommandHandler("sumsel", sumsel))
    dp.add_handler(CommandHandler("kalteng", kalteng))
    dp.add_handler(CommandHandler("sulut", sulut))
    dp.add_handler(CommandHandler("aceh", aceh))
    dp.add_handler(CommandHandler("sultenggara", sultenggara))
    dp.add_handler(CommandHandler("kep_riau", kep_riau))
    dp.add_handler(CommandHandler("lampung", lampung))
    dp.add_handler(CommandHandler("papua_barat", papua_barat))
    dp.add_handler(CommandHandler("ntb", ntb))
    dp.add_handler(CommandHandler("maluku", maluku))
    dp.add_handler(CommandHandler("kalimantan_utara", kalimantan_utara))
    dp.add_handler(CommandHandler("sulteng", sulteng))
    dp.add_handler(CommandHandler("bengkulu", bengkulu))
    dp.add_handler(CommandHandler("gorontalo", gorontalo))
    dp.add_handler(CommandHandler("jambi", jambi))
    dp.add_handler(CommandHandler("kalbar", kalbar))
    dp.add_handler(CommandHandler("maluku_itara", maluku_utara))
    dp.add_handler(CommandHandler("bangka", bangka))
    dp.add_handler(CommandHandler("ntt", ntt))
    dp.add_handler(CommandHandler("sulbar", ntt))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook(APP_NAME + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

http = urllib3.PoolManager()
# Create request to access Indonesian covid-19 data from Kawal Corona's API 
reqIndo = http.request('GET', 'https://api.kawalcorona.com/indonesia/')
dataIndo = json.loads(reqIndo.data.decode('utf-8'))

# Create request to access Indonesian covid-19 data from Kawal Corona's API 
reqProv = http.request('GET', 'https://api.kawalcorona.com/indonesia/provinsi')
dataProv = json.loads(reqProv.data.decode('utf-8'))

# Checking the bot
print('Bot is running...')

if __name__ == '__main__':
    main()
