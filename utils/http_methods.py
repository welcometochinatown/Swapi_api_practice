import requests

class HttpMethods():

    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=HttpMethods.headers, cookies=HttpMethods.cookie)
        return result