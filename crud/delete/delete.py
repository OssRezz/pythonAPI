import requests
import json

if __name__ == '__main__':
    url = 'https://httpbin.org/delete'
    payload = {'nombre': 'Eduardo','curso': 'pyton', 'nivel': 'intermedio'}
    headers = {'Conten-Type':'application/json', 'access-token':'12342'}

    response = requests.delete(url, data= json.dumps(payload), headers=headers)

    #json post se encarga de serializarlos
    #Si nosotros utilizamos data nos debemos encargar de serializarlos
    print(response.url)

    if response.status_code == 200:
        # print(response.content)
        #leer encabezados
        headers_reponse= response.headers #diccionario
        server = headers_reponse['Server']
        print(headers_reponse)
        #acceder a un parametro
        print(server)
        