from src.hh_parser import HH
from src.vacancy_saver import JSONFileSaver
from src.vacancy import Vacancy
from src.work_with_vacancy import filter_vacancies, sort_by_salary, get_top_vacancies, print_vacancies


def user_interaction():
    """
    Функция взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.
    """
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    hh = HH()
    sever = JSONFileSaver('C:/Users/denis.shtepa/bogdan.kozintsov/CodePractice/CW-4_HH_Api/data/vacancies.json')
    hh.load_vacancies(search_query)

    vacancy_objects = []
    for vacancy in hh.vacancies:
        vacancy_objects.append(Vacancy(vacancy["name"],
                                       vacancy["alternate_url"],
                                       vacancy["area"],
                                       vacancy["salary"],
                                       vacancy["salary"]["currency"],
                                       vacancy["employer"]))
    print(vacancy_objects)

    vacancy_dicts = []
    for vacancy_object in vacancy_objects:
        vacancy_dicts.append(vacancy_object.to_dict())

    # Сохранение вакансий в JSON-файл
    sever.save_to_json(vacancy_dicts)
    # for vac in vacancy_dicts:
    #     print(vac)

    # print(sort_by_salary(vacancy_dicts))
    # print_vacancies(sort_by_salary(get_top_vacancies(vacancy_dicts, 10)))
    # print_vacancies(filter_vacancies(sort_by_salary(get_top_vacancies(vacancy_dicts, 10))))

    # # # Создание экземпляра API и получение вакансий по поисковому запросу
    # hh = HH()
    # sever = JSONFileSaver('C:/Users/denis.shtepa/bogdan.kozintsov/CodePractice/CW-4_HH_Api/data/vacancies.json')
    # vacancy_objects = []
    # for vacancy in hh.vacancies:
    #     vacancy_objects.append(Vacancy(vacancy["name"],
    #                                    vacancy["alternate_url"],
    #                                    vacancy["area"],
    #                                    vacancy["salary"],
    #                                    vacancy["salary"]["currency"],
    #                                    vacancy["employer"]))
    #
    # vacancy_dicts = []
    # for vacancy_object in vacancy_objects:
    #     vacancy_dicts.append(vacancy_object.to_dict())
    #
    # sever.save(vacancy_dicts)
    # #     # Фильтрация, сортировка и выбор топ N вакансий
    # print(vacancy_dicts)
    #
    # if vacancy_dicts:
    #
    #     for vac in vacancy_dicts:
    #         print(vac)
    #         vacancy_dicts.append(vac)
    # Фильтрация, сортировка и выбор топ N вакансий
    # print(vacancy_dicts)
    filtered_vacancies = filter_vacancies(vacancy_dicts, filter_words)
    sorted_vacancies = sort_by_salary(filtered_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)
    # else:
    #     print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == '__main__':
    user_interaction()
