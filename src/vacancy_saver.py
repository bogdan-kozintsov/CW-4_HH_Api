import json


class JSONFileSaver:
    """Класс для сохранения вакансий в JSON-файл"""

    def __init__(self, file_path):
        """Инициализация JSONFileSaver"""
        self.file_path = file_path

    def save(self, vacancies):
        """Сохранение вакансий в JSON-файл"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get(self):
        """Загрузка вакансий из JSON-файла"""
        pass

    def delete(self):
        """Удаление JSON-файла"""
        pass
