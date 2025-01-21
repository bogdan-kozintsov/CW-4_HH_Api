import json
from abc import ABC, abstractmethod


class FileSaver(ABC):
    """Абстрактный класс для сохранения вакансий в файл"""

    @abstractmethod
    def save_to_json(self, vacancies):
        """Сохранение вакансий в JSON-файл"""
        pass

    @abstractmethod
    def get_from_json(self, keyword):
        """Получение вакансий из JSON-файла"""
        pass

    @abstractmethod
    def delete_from_json(self, keyword):
        """Удаление вакансий из JSON-файла"""
        pass


class JSONFileSaver(FileSaver):
    """Класс для сохранения вакансий в JSON-файл"""

    def __init__(self, file_path="data/vacancies.json"):
        """Инициализация JSONFileSaver"""
        self.file_path = file_path

    def save_to_json(self, vacancies):
        """Сохранение вакансий в JSON-файл"""
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_from_json(self):
        """Загрузка вакансий из JSON-файла"""
        pass

    def delete_from_json(self):
        """Удаление JSON-файла"""
        pass
