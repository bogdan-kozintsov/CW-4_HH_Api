from src.hh_parser import HH
from src.vacancy_saver import JSONFileSaver
from src.vacancy import Vacancy
from src.work_with_vacancy import filter_by_city, filter_by_key_word, sort_by_min_salary, get_top_vacancies, \
    print_vacancies


def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    city_name = input("Укажите город для фильтрации вакансий: ").split()
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh = HH()
    sever = JSONFileSaver('data/vacancies.json')
    hh.load_vacancies(search_query)

    vacancy_objects = []
    for vacancy in hh._vacancies:
        vacancy_objects.append(Vacancy(vacancy["name"],
                                       vacancy["alternate_url"],
                                       vacancy["area"],
                                       vacancy["salary"],
                                       vacancy["salary"]["currency"],
                                       vacancy["employer"]))

    vacancy_dicts = []
    for vacancy_object in vacancy_objects:
        vacancy_dicts.append(vacancy_object.to_dict())

    sever.save_to_json(vacancy_dicts)  # Сохранение вакансий в JSON-файл

    filtered_by_city = filter_by_city(vacancy_dicts, city_name)  # Фильтр по городу
    filtered_by_key_word = filter_by_key_word(filtered_by_city, filter_words)  # Фильтр по ключевым словам в названии
    sorted_vacancies = sort_by_min_salary(filtered_by_key_word)  # Сортировка по минимальной зарплате
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)  # Выборка топ N отсортированных вакансий
    print_vacancies(top_vacancies)  # Вывод выборки вакансий в консоль


if __name__ == '__main__':
    user_interaction()
