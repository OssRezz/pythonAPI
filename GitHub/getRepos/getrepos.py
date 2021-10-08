
import requests
client_id = ''
client_secret = ''
code = ''
access_token = ''

if __name__ == '__main__':
    
    url = 'https://api.github.com/user/repos'
    headers = {'Authorization' : 'token'}

    response = requests.get(url, headers=headers)
    if response.status_code == 200:

        payload = response.json()
        if payload:
            for repositorio in payload:
                name = repositorio['name']
                print(name)
    else:
        print(response.content)