from src.vacancy import Vacancy


def test_to_dict():
    vac = Vacancy("Тестировщик комфорта квартир",
                  "https://hh.ru/employer/3499705",
                  {"name": "Воронеж"},
                  {"from": 30000, "to": 44000, "currency": "RUR"},
                  {"name": "Яндекс Команда для бизнеса"}
                  )

    assert vac.to_dict() == {
        'Вакансия': 'Тестировщик комфорта квартир',
        'Работодатель': 'Яндекс Команда для бизнеса',
        'Город': 'Воронеж',
        'Зарплата от': 30000,
        'Зарплата до': 44000,
        'Валюта': 'RUR',
        'Ссылка на вакансию': 'https://hh.ru/employer/3499705'
    }


def test___lt__():
    vac1 = Vacancy("Тестировщик комфорта квартир",
                   "https://hh.ru/employer/3499705",
                   {"name": "Воронеж"},
                   {"from": 30000, "to": 44000, "currency": "RUR"},
                   {"name": "яндекс Команда для бизнеса"}
                   )
    vac2 = Vacancy("Разработчик Python",
                   "https://hh.ru/employer/3499705",
                   {"name": "Воронеж"},
                   {"from": 20000, "to": 30000, "currency": "RUR"},
                   {"name": "Яндекс Команда для бизнеса"}
                   )
    assert vac1 > vac2
