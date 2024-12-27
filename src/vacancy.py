from src.hh_parser import HH

class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, name, alternate_url, area, salary, currency, employer):
        """Инициализация вакансии"""
        self.name = name
        self.alternate_url = alternate_url
        self.area = area['name']
        self.salary_from = salary.get('from')
        self.salary_to = salary.get('to')
        self.salary = \
            f'{self.salary_from} - {self.salary_to} {currency}' if self.salary_from and self.salary_to else 'Не указано'
        self.employer = employer['name']


    # def to_list(self):
    #     """Получение списка вакансиq"""
    #     hh = HH()
    #     vacancy_objects = []
    #     for vacancy in hh.vacancies:
    #         vacancy_objects.append(Vacancy(vacancy["name"],
    #                                        vacancy["alternate_url"],
    #                                        vacancy["area"],
    #                                        vacancy["salary"],
    #                                        vacancy["salary"]["currency"],
    #                                        vacancy["employer"]))


    def to_dict(self):
        """Получение словаря вакансии в формате JSON"""
        return {
            'Вакансия': self.name,
            'Работодатель': self.employer,
            'Город': self.area,
            'Зарплата': self.salary,
            'Ссылка на вакансию': self.alternate_url
        }

    def __repr__(self):
        """Представление вакансии в текстовом виде"""
        return (f'Название: {self.name}\n'
                f'URL: {self.alternate_url}\n'
                f'Area: {self.area}\n'
                f'Salary: {self.salary}\n'
                f'Employer: {self.employer}')

    def __lt__(self, other):
        return self.salary < other.salary
