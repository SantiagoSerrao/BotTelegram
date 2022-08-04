from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from engine import get_chiste, get_ips, get_hash , read_alerts , get_alerts , promoteAlertToPhishCase , promoteAlertToIncidentCase
import yaml, logging, os, time
import schedule
from thehive4py.api import TheHiveApi
from thehive4py.models import *
from thehive4py.query import *

""" Variable Semaforo Estados en la Conversacion """
INPUT_TEXT = 0 

""" Funciones """
def start(update, context):
    logger.info('He recibido un comando start')
    update.message.reply_text('¡Hola %s este es un bot usado con The Hive !' % update.message.from_user.name)

def leerAlertas(update,context):
    logger.info('Leyendo ultima alerta')
    update.message.reply_text(read_alerts())
def alertas(update,context):
    alerts = [] 
    logger.info('Consultando Alertas')
    alerts  =  get_alerts()
    longitud= len(alerts)
    if  longitud != 0:
        for i in alerts:
            update.message.reply_text(i['description'])
    else:
        update.message.reply_text('No hay alertas nuevas! Tomate un cafecito ' + '\U0001F917')
        
# function to promote a case to pish case in the hive platform        
def alertToPhishCase(update,context):
    logger.info('Promoviendo alerta a un caso')
    update.message.reply_text('Es necesario que me pases el alert id para crear el caso %s.' % update.message.from_user.name)
    return INPUT_TEXT
def creatPhishCase(update,contenxt):
    logger.info('Se recibio el id para crear el caso')
    alert_id = update.message.text
    promoteAlertToPhishCase(alert_id)
    update.message.reply_text('Caso de posible phishing creado correctamente' + '\U0001F600')
    logger.info('OK')
    update.message.text = ''
    return ConversationHandler.END


# function to promote a case to incident case in the hive platform  
def alertToIncidentCase(update,context):
    logger.info('Promoviendo alerta a un caso')
    update.message.reply_text('Es necesario que me pases el alert id para crear el caso %s.' % update.message.from_user.name)
    return INPUT_TEXT
def creatIncidentCase(update,contenxt):
    logger.info('Se recibio el id para crear el caso')
    alert_id = update.message.text
    promoteAlertToIncidentCase(alert_id)
    update.message.reply_text('Incidente creado correctamente' + '\U0001F600')
    logger.info('OK')
    update.message.text = ''
    return ConversationHandler.END



""" Main del Programa """
if __name__ == '__main__':

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    logger = logging.getLogger('Hive_Bot')

    """ Llave API para conectarse a Telegram """
    updater = Updater(token=os.getenv("TOKEN_TELEGRAM"), use_context=True)
    dp = updater.dispatcher

    """ Handler's """
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('leerAlertas',leerAlertas ))
    dp.add_handler(CommandHandler('alertas', alertas ))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('crearCasoPhish', alertToPhishCase)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, creatPhishCase)]
        },
        fallbacks=[]
    ))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('crearIncidente', alertToIncidentCase)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, creatIncidentCase)]
        },
        fallbacks=[]
    ))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('ioc', ioc)
        ],
        states={
            INPUT_TEXT: [MessageHandler(Filters.text, updateIoc)]
        },
        fallbacks=[]
    ))

    updater.start_polling()
    updater.idle()
