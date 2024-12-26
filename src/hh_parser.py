import json

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
        self.params = {'text': '', 'page': 0, 'per_page': 100, 'area': 113, 'salary': 100000, 'only_with_salary': True}
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

    def __init__(self, name, alternate_url, area, salary, currency, employer):
        self.name = name
        self.alternate_url = alternate_url
        self.area = area['name']
        self.salary_from = salary.get('from')
        self.salary_to = salary.get('to')
        self.salary = f'{self.salary_from} - {self.salary_to} {currency}' if self.salary_from and self.salary_to else 'Не указано'
        self.employer = employer['name']

    def to_dict(self):
        return {
            'Вакансия': self.name,
            'Работодатель': self.employer,
            'Город': self.area,
            'Зарплата': self.salary,
            'Ссылка на вакансию': self.alternate_url
        }

    def __repr__(self):
        return (f'Название: {self.name}\n'
                f'URL: {self.alternate_url}\n'
                f'Area: {self.area}\n'
                f'Salary: {self.salary}\n'
                f'Employer: {self.employer}')


class JSONFileSaver:
    """Класс для сохранения вакансий в JSON-файл"""

    def __init__(self, file_path):
        self.file_path = file_path

    def save(self, vacancies):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__':
    hh = HH()
    sever = JSONFileSaver('C:/Users/denis.shtepa/bogdan.kozintsov/CodePractice/CW-4_HH_Api/data/vacancies.json')
    hh.load_vacancies('водитель')

    vacancy_objects = []
    for vacancy in hh.vacancies:
        vacancy_objects.append(Vacancy(vacancy["name"],
                                       vacancy["alternate_url"],
                                       vacancy["area"],
                                       vacancy["salary"],
                                       vacancy["salary"]["currency"],
                                       vacancy["employer"]))

    vacancy_dicts = []
    for vacancy_object in vacancy_objects:
        vacancy_dicts.append(vacancy_object.to_dict())

    sever.save(vacancy_dicts)
