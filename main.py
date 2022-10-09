#HOLA NANO
#Hola git pull command :)
bot_token = "5756497503:AAGupePh024UdwwUu3kePQDJ7ziDY5jWfdY"

from telegram import Update
from telegram.ext import Updater, ContextTypes #SEND MESSAGES
import logging #LOGEO
from telegram.ext import CommandHandler, MessageHandler, Filters #COMANDOS

from datetime import datetime

updater = Updater(token = bot_token, use_context = True)
dispatcher = updater.dispatcher

#Loggin Start
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#COMANDOS
def start(update: Update, context: ContextTypes):
    print(f"\nId nueva: {update.effective_chat.id}") #ESCRIBE EL CHAT ID DE LA PERSONA
    print(f"\nUsername: {update.effective_user.username}")
    #ALMACENA EL CHAT ID A EL ARCHIVO: personas/personas.txt
    archivo = open('personas/personas.txt', 'a')
    archivo.write(str(update.effective_chat.id)+"\n")
    archivo.close()

    archivo = open('personas/usernames.txt', 'a')
    archivo.write(str(update.effective_user.username)+"\n")
    archivo.close()
    
#    timeHour = datetime.now().strftime('%H:%M')

    text2 = f"Hola! {update.effective_user.first_name} :)\n _Cuentame lo que quieras_"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text2, parse_mode="Markdown") # BOT'S RESPOND

#FUNCIONES

def echo(update:Update, context:ContextTypes):
    update.message.reply_text(update.message.text, entities=update.message.entities)


def newMessage(update:Update, context:ContextTypes):
    print(f"\n{update.effective_user.username}: {update.message.text} | {update.message.date}\nEnviar Mensaje: ", end='')
    
    archivo = open(f"registros/{update.effective_user.username}.txt", 'a')
    archivo.write(str(f"{update.message.date}: {update.message.text}\n"))
    archivo.close()
    

#eventos de comandos
start = CommandHandler('start', start) #LLAMA A LA FUNCION start CON EL COMANDO /start
dispatcher.add_handler(start) #ANADE EL COMANDO PARA QUE FUNCIONE
#eventes de mensajes
newMessag = MessageHandler(Filters.text, newMessage)
dispatcher.add_handler(newMessag)

updater.start_polling() #ENCIENDE EL BOT, PARA PARAR updater.stop()

#USAR SIN COMANDOS, NO HACE FALTA EL USO DE LO DE ARRIBA, SALVO el "bot_token" Y LA LISTA DE CHAT-IDs
#LIBRERIAS SIN RESPONDER
from telegram import Bot, User #ENVIAR MENSAJES SIN RESPONDER
from telegram import MessageEntity

#ENVIAR A SUBSCRIPTORES
def sendMessage(h):
    # bold - italic - url - cashtag - code - email - custom_emoji - hashtag - mention - spoiler
    # bot_command - phone_number - underline - pre - strikethrough - text_link - text_mention - 
    #
    # Markdown V1 Sintax
    #   bold: *text*    -   italic: _text_  -   link: [text](url)  -   code: `text` 
    
    personasLista = [] #CREA LISTA
    with open('personas/personas.txt', 'r') as archivo: #OBTIENE CHAT IDs OBTENIDOS GRACIAS A /personas
        for personaLinea in archivo:
            persona = personaLinea[:-1]
            personasLista.append(persona)
    for i in personasLista: #MANDA UN MENSAJE A CADA UNO DE LAS subscripciones
        bot = Bot(bot_token) #DEFINE "bot" A NUESTRO TOKEN
        
        bot.send_message(chat_id=i,text=h, parse_mode="Markdown") #MANDA MENSAJE
#        bot.send_message(chat_id=i,text=f"{h}", entities=[entiti]) #MANDA MENSAJE
        


while True:
    h = input("Enviar mensaje: ")
    sendMessage(h)
