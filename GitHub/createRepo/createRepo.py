import requests


if __name__ == '__main__':
    client_id = ''
    client_secret = ''
    code = ''

    access_token = ''
    
    url = 'https://api.github.com/user/repos'
    payload = {'name' : 'git_api_cff_comunidad'}
    headers = {'Accept':'application/json','Authorization' : 'token ' + access_token}

    response = requests.post(url, headers=headers, json=payload)
    print(response.status_code)

    if response.status_code == 200:
        print(response.json())

    else:
        print(response.content)

