import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный родительский класс для работы с API"""

    @abstractmethod
    def load_vacancies(self, keyword):
        """Загрузка вакансий из API"""
        pass


class HH(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        """Инициализация клиента для работы с API HeadHunter"""
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 100, 'only_with_salary': True, 'area': 113}
        self._vacancies = []

    @property
    def vacancies(self):
        return self._vacancies

    def load_vacancies(self, keyword):
        """Загрузка вакансий с поискового запроса"""
        self.__params['text'] = keyword
        while self.__params.get('page') != 3:
            response = requests.get(self.__url, headers=self.__headers, params=self.__params)
            _vacancies = response.json()['items']
            self._vacancies.extend(_vacancies)
            self.__params['page'] += 1
