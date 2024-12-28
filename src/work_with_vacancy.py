def filter_by_city(vacancies, city_name):
    """
    Фильтрует список вакансий по ключевым словам в описании.
    """

    return [vacancy for vacancy in vacancies if
            any(key.title() in vacancy['Город'].title() for key in city_name)]


def filter_by_key_word(vacancies, filter_words):
    """
    Фильтрует список вакансий по ключевым словам в описании.
    """

    return [vacancy for vacancy in vacancies if
            any(key.lower() in vacancy['Вакансия'].lower() for key in filter_words)]


def sort_by_min_salary(vacancies):
    """
    Сортирует список вакансий по убыванию зарплаты.
    """
    return sorted(vacancies, key=lambda vacancy: vacancy['Зарплата от'], reverse=True)


def get_top_vacancies(vacancies, upper_part):
    """
    Возвращает верхнюю часть списка вакансий в соответствии с указанным лимитом.
    """
    return vacancies[:upper_part]


def print_vacancies(vacancies):
    """
    Выводит информацию о вакансиях в консоль.
    """
    if vacancies:
        for index, vacancy in enumerate(vacancies, start=1):
            print(f"\nВакансия: {index}: {vacancy.get('Вакансия')}\n"
                  f"Работодатель - {vacancy.get('Работодатель')}\n"
                  f"Город - {vacancy.get('Город')}\n"
                  # f"Зарплата: {vacancy.get('Зарплата')} {vacancy.get('Валюта')}\n"
                  f"Зарплата от {vacancy.get('Зарплата от')} до {vacancy.get('Зарплата до')} {vacancy.get('Валюта')}\n"
                  # f"Средняя зарплата: {vacancy.get('Средняя зарплата')} {vacancy.get('Валюта')}\n"
                  f"Ссылка на вакансию: {vacancy.get('Ссылка на вакансию')}")

        print(f"\nВсего вакансий: {len(vacancies)}")
    else:
        print("Нет подходящих вакансий")
