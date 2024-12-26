import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """Абстрактный класс для парсинга вакансий"""

    @abstractmethod
    def load_vacancies(self):
        """Загрузка вакансий из API"""
        pass


class HH:
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 3:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, name, alternate_url):
        self.name = name
        self.alternate_url = alternate_url

    def __repr__(self):
        return f'\nНазвание: {self.name}, URL: {self.alternate_url}'


if __name__ == '__main__':
    hh = HH()
    hh.load_vacancies('Python')

    vacancy_objects = []
    for vacancy in hh.vacancies:
        vacancy_objects.append(Vacancy(vacancy["name"], vacancy["alternate_url"]))

    print(vacancy_objects)
