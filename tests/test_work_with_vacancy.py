from src.work_with_vacancy import (filter_by_city,
                                   filter_by_key_word,
                                   sort_by_min_salary,
                                   get_top_vacancies)


def test_filter_by_city():
    vacancies = [{'Город': 'Москва'},
                 {'Город': 'Москва'},
                 {'Город': 'Воронеж'},
                 {'Город': 'Минск'},
                 {'Город': 'Саратов'}]
    assert len(filter_by_city(vacancies, "Москва")) == 2
    assert len(filter_by_city(vacancies, "Воронеж")) == 1


def test_filter_by_key_word():
    vacancies = [{'Вакансия': 'Разработчик Python'},
                 {'Вакансия': 'Разработчик Java'},
                 {'Вакансия': 'Тестировщик'},
                 {'Вакансия': 'Менеджер проектов'}]
    # assert len(filter_by_key_word(vacancies, "Разработчик")) == 2
    assert len(filter_by_key_word(vacancies, "Тестировщик")) == 1


def test_sort_by_min_salary():
    vacancies = [{'Зарплата от': 100000, 'Зарплата до': 150000},
                 {'Зарплата от': 150000, 'Зарплата до': 200000},
                 {'Зарплата от': 120000, 'Зарплата до': 180000}]
    assert sort_by_min_salary(vacancies)[0]['Зарплата от'] == 150000
    assert sort_by_min_salary(vacancies)[1]['Зарплата от'] == 120000


def test_get_top_vacancies():
    vacancies = [{'Вакансия': 'Разработчик Python'},
                 {'Вакансия': 'Разработчик Java'},
                 {'Вакансия': 'Тестировщик'},
                 {'Вакансия': 'Менеджер проектов'}]
    assert len(get_top_vacancies(vacancies, 2)) == 2
    assert len(get_top_vacancies(vacancies, 1)) == 1
    assert len(get_top_vacancies(vacancies, 6)) == 4
