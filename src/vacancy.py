class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, name, alternate_url, area, salary, currency, employer):
        """Инициализация вакансии"""
        self.name = name
        self.alternate_url = alternate_url
        self.area = area['name']
        self.salary_from = salary.get('from') if salary.get('from') else 0
        self.salary_to = salary.get('to') if salary.get('to') else '"всё зависит только от тебя"'
        # self.salary = \
        #     f'{self.salary_from} - {self.salary_to}' if self.salary_from or self.salary_to else 0
        # self.avg_salary = int((self.salary_from + self.salary_to) / 2) \
        #     if self.salary_from != 0 and self.salary_to != 0 else self.salary
        self.currency = currency
        self.employer = employer['name']


    def to_dict(self):
        """Получение словаря вакансии в формате JSON"""
        return {
            'Вакансия': self.name,
            'Работодатель': self.employer,
            'Город': self.area,
            # 'Зарплата': self.salary,
            'Зарплата от': self.salary_from,
            'Зарплата до': self.salary_to,
            'Валюта': self.currency,
            # 'Средняя зарплата': self.avg_salary,
            'Ссылка на вакансию': self.alternate_url
        }

    def __repr__(self):
        """Представление вакансии в текстовом виде"""
        return (f'Название: {self.name}\n'
                f'URL: {self.alternate_url}\n'
                f'Area: {self.area}\n'
                f'Salary_from: {self.salary_from}\n'
                f'Salary_to: {self.salary_to}\n'
                f'Currency: {self.currency}\n'
                f'Employer: {self.employer}')

    def __lt__(self, other):
        return self.salary_from < other.salary_from
