import requests


def send_email(stockstatus):
    key = '4f40d6c46a651e99e3be90e89ee86e43-9ad3eb61-49aa7a99'
    #key = '7b5599a9cbc97233ca7fef30dbe5d456-0a4b0c40-199144e1'

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
