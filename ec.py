import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('1886052065:AAFkiha4Hr9c5P6Apsd3bophVu_qIIw4tQ4') 
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['hola']) 
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id,  "HOLA, Envia  GB o gb para ver formula Gigabytes a Megabytes \n Envia TB o tb para ver formula Terabytes a Gigabytes \n Envia MB o mb para ver formula Megabytes a Kilobytes \n Envia  b o B para ver formula Bytes a bits \n ")
    print("Mandaron opcion")

@bot.message_handler(commands=['gb','GB']) 
def GB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Multiplica el valor de tamaño de datos por 1024")
    print("Mandaron gb ,GB")

@bot.message_handler(commands=['tb','TB'])
def TB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Multiplica el valor de tamaño de datos por 1024")
    print("Mandaron tb, TB")

@bot.message_handler(commands=['mb','MB'])
def MB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Multiplica el valor de tamaño de datos por 1024")
    print("Mandaron ,mb ,MB")

@bot.message_handler(commands=['b','B'])
def b(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "Multiplica el valor de tamaño de datos por 8")
    print("Mandaron b")

bot.polling()