def filter_vacancies(vacancies, key_words):
    """
    Фильтрует список вакансий по ключевым словам в описании.
    """

    return [vacancy for vacancy in vacancies if
            any(key.lower() in vacancy['Вакансия'].lower() for key in key_words)]


def sort_by_salary(vacancies):
    """
    Сортирует список вакансий по убыванию зарплаты.
    """
    return sorted(vacancies, key=lambda vacancy: vacancy['Зарплата'], reverse=True)


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
            # print(f"Вакансия {index}:")
            # print(f"Название: {vacancy.get('name', 'Не указано')}")
            # print(f"Зарплата от: {vacancy.get('salary_from', 'Не указана')}")
            # print(f"Описание: {vacancy.get('description', 'Отсутствует')}")
            # print(f"Ссылка: {vacancy.get('alternate_url', 'Не указана')}")
            # print()
            print(f"Вакансия {index}: {vacancy.get('Вакансия')}\n"
                  f"Работодатель {vacancy.get('Работодатель')}\n"
                  f"Город {vacancy.get('Город')}\n"
                  f"Зарплата {vacancy.get('Зарплата')}\n"
                  f"Ссылка на вакансию {vacancy.get('Ссылка на вакансию')}\n")



        print(f"Всего вакансий: {len(vacancies)}")
    else:
        print("Нет подходящих вакансий")