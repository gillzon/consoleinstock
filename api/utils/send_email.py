import requests
import os


def send_email(stockstatus):
    key = os.environ['MAILGUN_KEY']

    domain = 'mg.oscargillberg.se'
    recipient = 'oscargillberg@gmail.com'

    request_url = 'https://api.eu.mailgun.net/v3/{0}/messages'.format(domain)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'playstation5stockstatus@oscargillberg.se',
        'to': recipient,
        'subject': 'Playstation 5 netonet lagerstatus',
        'text': '{0}'.format(stockstatus)
    })
    print(request.status_code)
    print(request.text)
