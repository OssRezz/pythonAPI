import requests


if __name__ == '__main__':

    
    url = 'https://httpbin.org/cookies'
    cookies = {'my-cookie' : 'James'}
    headers = {'Accept':'application/json'}

    response = requests.get(url, headers=headers, cookies=cookies)

    #return true or false .ok
    if response.ok:
        cookies = response.cookies
        print(cookies)

        print("El contenido es :")
        print(response.content)


