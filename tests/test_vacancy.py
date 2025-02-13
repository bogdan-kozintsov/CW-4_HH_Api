from src.vacancy import Vacancy


def test_to_dict():
    vacancy = Vacancy('Python Developer',
                      'https://hh.ru/vacancy/234567',
                      'Москва',
                      'от 100000 до 200000',
                      'руб.',
                      'Яндекс')
    assert vacancy.to_dict() == {
        'Вакансия': 'Python Developer',
        'Работодатель': 'Яндекс',
        'Город': 'Москва',
        'Зарплата от': '150 000',
        'Зарплата до': '250 000',
        'Валюта': 'руб.',
        'Ссылка на вакансию': 'https://hh.ru/vacancy/234567'
    }
