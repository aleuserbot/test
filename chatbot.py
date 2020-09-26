import telebot

API_TOKEN = '1251369204:AAFcHbjzDGri_TI_Z-IBdjDH8h4xkRaWniE'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
ciao Sono Bot Per Chattare con te.\
""")

@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message,'se ti serve aiuto contatta @userbot22 grazie')

@bot.message_handler(commands=['Gruppo'])
def send_welcome(message):
    bot.reply_to(message, "test [https://google.com]", parse_mode='MarkdownV2')   

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text=='ciao':
        bot.reply_to(message, 'Ciao A te Come Stai?')
    elif message.text=='Bene':
        bot.reply_to(message, 'Mi Fa Piacere :)')
    elif message.text=='anche a me':
        bot.reply_to(message, 'Grazie.')
    elif message.text=='che fai di bello?':
        bot.reply_to(message, 'Mi Annoio te in vece?')
    elif message.text=='bho':
        bot.reply_to(message, 'a bella risposta bho')
    elif message.text=='avete un canale per gli Aggiornamenti del bot questo?':
        bot.reply_to(message, 'si \n e questo \n\n⬇️ \n\n@pybotStatusCanale')
    else:
        bot.reply_to(message, 'Mi dispiace Ma questo messaggio che hai inviato ho un comando Non lo trovo nel Archivio mio mi dispiace molto.')


bot.polling()
