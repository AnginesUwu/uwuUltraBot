#HOLA NANO
#Hola git pull command :)
bot_token = "5756497503:AAGupePh024UdwwUu3kePQDJ7ziDY5jWfdY"

from telegram import Update
from telegram.ext import Updater, ContextTypes #SEND MESSAGES
import logging #LOGEO
from telegram.ext import CommandHandler #COMANDOS

from datetime import datetime

updater = Updater(token = bot_token, use_context = True)
dispatcher = updater.dispatcher

#Loggin Start
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#CODE
def start(update: Update, context: ContextTypes):
    timeHour = datetime.now().strftime('%H:%M')

    print(update.effective_chat.id) #print the ID of the User
    text2 = "hola " + str(update.effective_user.first_name) + "\n Son las " + str(timeHour)
    context.bot.send_message(chat_id=update.effective_chat.id, text=text2) # BOT'S RESPOND

def personas(update: Update, context: ContextTypes):
    print(update.effective_chat.id) #ESCRIBE EL CHAT ID DE LA PERSONA
    #ALMACENA EL CHAT ID A EL ARCHIVO: personas/personas.txt
    archivo = open('personas/personas.txt', 'a')
    archivo.write(str(update.effective_chat.id)+"\n")
    archivo.close()
    
    context.bot.send_message(chat_id=update.effective_chat.id, text="AHORA ESTÁS EN LA LISTA!!") #RESPONDE A EL CHAT EN EL QUE LE HABLAN
    

start = CommandHandler('start', start) #LLAMA A LA FUNCION start CON EL COMANDO /start
personas = CommandHandler('personas', personas) #LLAMA A LA FUNCION personas CON EL COMANDO /personas
dispatcher.add_handler(start) #ANADE EL COMANDO PARA QUE FUNCIONE
dispatcher.add_handler(personas) #ANADE EL COMANDO PARA QUE FUNCIONE

updater.start_polling() #ENCIENDE EL BOT, PARA PARAR updater.stop()

#USAR SIN COMANDOS, NO HACE FALTA EL USO DE LO DE ARRIBA, SALVO el "bot_token" Y LA LISTA DE CHAT-IDs
#LIBRERIAS SIN RESPONDER
from telegram import Bot, User #ENVIAR MENSAJES SIN RESPONDER

#ENVIAR SIN RESPONDER
def enviarSinResponder(h):
    personasLista = [] #CREA LISTA
    with open('personas/personas.txt', 'r') as archivo: #OBTIENE CHAT IDs OBTENIDOS GRACIAS A /personas
        for personaLinea in archivo:
            persona = personaLinea[:-1]
            personasLista.append(persona)
    for i in personasLista: #MANDA UN MENSAJE A CADA UNO DE LAS PERSONAS QUE HAY EN EL ARCHIVO
        bot = Bot(bot_token) #DEFINE "bot" A NUESTRO TOKEN
        
        bot.send_message(chat_id=i,text=f"{h}") #MANDA MENSAJE
while True:
    h = input("Enviar mensaje: ")
    enviarSinResponder(h)
