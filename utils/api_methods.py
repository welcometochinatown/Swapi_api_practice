from utils.http_methods import HttpMethods

class SwapiApi():

    @staticmethod
    def get_from_swapi(url):

        get_url = url
        # print(get_url)
        result_get = HttpMethods.get(get_url)
        return result_get