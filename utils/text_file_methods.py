

class TextFiles():

    @staticmethod
    def create_text_file(path):
        """Создание файла"""

        with open(path, "w", encoding="utf-8") as file:
            file.write("")

    @staticmethod
    def add_to_text_file(path, argument):
        """Создание текстового файла и запись argument"""

        with open(path, "a", encoding="utf-8") as file:
            file.write(argument + "\n")