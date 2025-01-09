import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для парсинга вакансий"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Загрузка вакансий из API"""
        pass


class HH(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        """Инициализация клиента для работы с API HeadHunter"""
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_salary': True, 'area': 113}
        self.vacancies = []

    def load_vacancies(self, keyword):
        """Загрузка вакансий с поискового запроса"""
        self.params['text'] = keyword
        while self.params.get('page') != 3:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
