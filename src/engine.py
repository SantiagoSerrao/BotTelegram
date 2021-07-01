import requests, json, iocextract
from thehive4py.api import TheHiveApi
from thehive4py.models import *
from thehive4py.query import *

THEHIVE_URL = 'http://10.162.1.124:9000'
THEHIVE_API_KEY = 'YEvjNWm5EZtYVV7biWb84qLxB+0wV0+T'
api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)

""" Chiste de Prueba """
def get_chiste():

    joke=requests.get('https://api.chucknorris.io/jokes/random')
    data=joke.json()

    return data["value"]

def get_alerts():
    array_alerts = []
    query=  (
        (Eq('status','New'))
    )
    response = api.find_alerts(query=query)
    text= json.loads(response.text)
    for alerts in text:
        array_alerts.append(alerts)


    return array_alerts


def read_alerts():
    query=  (
        (Eq('status','New'))
    )

    response = api.find_alerts(query=query)
    json_data = json.loads(response.text)

    #recorro y voy marcando como leido
    for clave in json_data:
        api.mark_alert_as_read(clave['id'])
        return 'Alerta leida ' +  clave['id']

def promoteAlertToPhishCase(alert_id):
        api.promote_alert_to_case(alert_id, case_template='Phishing_Case')

def promoteAlertToIncidentCase(alert_id):
    api.promote_alert_to_case(alert_id, case_template='Incident_Investigation')

""" Parseo del Contenido IP's | Hash """
def get_ips(content):
    array_ips = []
    for ips in iocextract.extract_ips(content):
        array_ips.append(ips)
    return array_ips

def get_hash(content):
    array_hashes = []
    for hashes in iocextract.extract_hashes(content):
        array_hashes.append(hashes)
    return array_hashes