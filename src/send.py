from urllib.parse import urlencode 
from urllib.request import Request, urlopen
from datetime import datetime
import json, logging, time, telegram, os, schedule

""" Variables """
today = datetime.today().strftime('%Y%m%d')
token = os.getenv("TOKEN_TELEGRAM")

chat_id = -

""" Functions """


def get_notification():
    logger.info('Consultando API VulDB')
    if (json['response']['status'] == '200'):
        logger.info('API VulDB Status: %s' % json['response']['status'])
        texto = get_vulnerabilities(json, today)
    else:
        logger.warning('API VulDB Status: %s' % json['response']['status'])
        texto = 'Imposible comunicarme con la API'
    return texto

def send_message(token, chat_id, msg):
    bot = telegram.Bot(token=token)
    if len(msg) > 4096: 
        for x in range(0, len(msg), 4096): 
            bot.send_message(chat_id=chat_id, text=msg[x:x+4096]) 
    else: 
        bot.send_message(chat_id=chat_id, text=msg)
            

""" Logging """
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger('HiveBot')
logging.getLogger('schedule').setLevel(logging.CRITICAL + 10)
logger.info('······ WELCOME TO TELEGRAM THE_HIVE BOT ······')


