class Vacancy:
    """Класс для представления вакансии"""

    def __init__(self, name, alternate_url, area, salary, employer):
        """Инициализация вакансии"""
        self.name = name
        self.alternate_url = alternate_url
        self.area = area['name']
        self.salary_from = salary.get('from') if salary.get('from') else 0
        self.salary_to = salary.get('to') if salary.get('to') else '...'
        self.currency = salary.get('currency') if salary.get('currency') else 'у/е'
        self.employer = employer['name']

    def to_dict(self):
        """Получение словаря вакансии в формате JSON"""
        return {
            'Вакансия': self.name,
            'Работодатель': self.employer,
            'Город': self.area,
            'Зарплата от': self.salary_from,
            'Зарплата до': self.salary_to,
            'Валюта': self.currency,
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
