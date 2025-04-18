from utils.api_methods import SwapiApi
from utils.text_file_methods import TextFiles
from utils.checking import Checking


class TestNewRequest():

    @staticmethod
    def test_swapi_api(set_up):

        # Базовый URL
        base_url = "https://swapi.info/api/people/4/"

        # Пути к текстовым файлам
        local_txt_path = ".\\names_from_requests\\character_names.txt"

        # Создаем текстовый файл по указанному пути
        TextFiles.create_text_file(local_txt_path)

        # Список имен персонажей
        names = []

        # Отправляем GET запрос по заданному URL, выводим статус код и список фильмов с Дарт Вейдером
        print("First GET request")
        result_get = SwapiApi.get_from_swapi(base_url)
        Checking.check_status_code(result_get, 200)
        result_json = result_get.json()
        print(f"Список URL фильмов по запросу :\n {result_json['films']}")

        for films in result_json['films']:
            """Цикл для работы с фильмами из списка фильмов полученных ранее"""

            resul_get_film = SwapiApi.get_from_swapi(films)
            Checking.check_status_code(resul_get_film, 200)
            result_json = resul_get_film.json()
            print(f"Список URL персонажей по запросу :\n {result_json['characters']}")

            for character in result_json['characters']:
                """Цикл для работы с именами из списка персонажей полученных ранее"""

                result_get_name = SwapiApi.get_from_swapi(character)
                # Checking.check_status_code(result_get_name, 200)
                result_json = result_get_name.json()
                # print(result_json['name'])

                # Если имени нет в новом списке names, то добавляем его (убираем дубли)
                if result_json['name'] not in names:
                    names.append(result_json['name'])

        print("\nСписок всех персонажей, которые снимались в фильмах с Дарт Вейдером : ")
        for n in names:
            """Выводим имена из финального списка после сортировок и добавляем их в текстовый файл"""
            print(f"Имя киногероя : {n}")
            TextFiles.add_to_text_file(local_txt_path, n)
