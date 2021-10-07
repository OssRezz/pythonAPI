import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/post'
    payload = {'nombre': 'Eduardo','curso': 'pyton', 'nivel': 'intermedio'}
    headers = {'Conten-Type':'application/json', 'access-token':'12342'}

    response = requests.post(url, data= json.dumps(payload), headers=headers)


    print(response.url)

    if response.status_code == 200:
        # print(response.content)
        #leer encabezados
        headers_reponse= response.headers #diccionario
        server = headers_reponse['Server']
        #acceder a un parametro
        print(server)
        