import requests
if __name__ == '__main__':
    url = 'https://httpbin.org/get'

    args = {'nombre': 'Eduardo','curso': 'pyton', 'nivel': 'intermedio'}
    response = requests.get(url, params=args)
    print(response.url)
    if response.status_code == 200:
        content = response.content
        print(content)