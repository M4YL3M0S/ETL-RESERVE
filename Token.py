import requests

# urls
reserve_base_url = "https://api.reserve.com.br/api/core"
access_url = '/acesso'


def authenticate():
    response = requests.post(reserve_base_url + access_url,
                             headers={'Content-Type': 'application/json'},
                             data='{"IdLicenciado": "2280","Usuario": "12191894640","Senha": "Mm200517"}')
    header = {
        'SecurityToken': response.json(),
        'Content-Type': 'application/json'
    }
    return header