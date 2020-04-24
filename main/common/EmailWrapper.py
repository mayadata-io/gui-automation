import requests


def get_email(email):
    url = "http://preview.putsbox.com/p/%s/last.json" % email.replace('@putsbox.com', '')
    headers = {'Content-type': 'xml'}
    r = requests.get(url=url)
    data = r.json()
    yield data