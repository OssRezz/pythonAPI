import requests

from requests.models import Response

if __name__ == '__main__':
    url = 'https://i.imgur.com/ZccahuC.jpeg'
    
    #realiza la peticion sin descargar el contenido (Esto es para mantener la conexion abierta)
    response = requests.get(url, stream=True)
    with open('image.jpg','wb') as file:

        #toma todo el contenido y lo descarga poco a poco
        #importante para archivos pesados
        for chunk in response.iter_content():
            file.write(chunk)

    #cerramos la conexion
    response.close()
        