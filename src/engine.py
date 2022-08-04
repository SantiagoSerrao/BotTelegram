import requests, json, iocextract
from thehive4py.api import TheHiveApi
from thehive4py.models import *
from thehive4py.query import *

THEHIVE_URL = ''
THEHIVE_API_KEY = ''
# place to put the url and the api key
api = TheHiveApi(THEHIVE_URL, THEHIVE_API_KEY)


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

    #run and read the alerts
    for clave in json_data:
        api.mark_alert_as_read(clave['id'])
        return 'Alerta leida. En caso que quieras crear un caso vas a tener que darme el alert ID. De esta alerta el alert id es: ' +  clave['id']

def promoteAlertToPhishCase(alert_id):
    api.promote_alert_to_case(alert_id, case_template='Phishing_Case')


def promoteAlertToIncidentCase(alert_id):
    api.promote_alert_to_case(alert_id, case_template='Incident_Investigation')

