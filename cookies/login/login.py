import requests

if __name__ == '__main__':
    url = 'https://api.github.com/user'

    session = requests.session()
    session.auth = ('','')

    response=session.get(url)

    if response.ok:
        print(response.content)
    else:
        print(response.content)
        response = session.get('https://github.com/')
        if response.ok:
            print(response.cookies['_gh_sess'])