from src.hh_parser import HH
from src.vacancy_saver import JSONFileSaver
from src.vacancy import Vacancy


def user_interaction(self):
    """
    Функция взаимодействия с пользователем для поиска, фильтрации и вывода вакансий с сайта HH.ru.
    """
    pass
    # search_query = input("Введите поисковый запрос: ")
    # top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    # filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    #
    # # Создание экземпляра API и получение вакансий по поисковому запросу
    # hh_api = HHapi()
    # hh_vacancies = hh_api.get_vacancies(search_query)
    # saver = JSONSaver()
    # saver.write_data(hh_vacancies)
    # print("Ответ API:", hh_vacancies)
    #
    # if hh_vacancies:
    #     vacancies_list = []
    #
    #     for vac in hh_vacancies:
    #         print(vac)
    #         vacancies_list.append(vac)
    #     # Фильтрация, сортировка и выбор топ N вакансий
    #     print(vacancies_list)
    #     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    #     sorted_vacancies = sort_vacancies(filtered_vacancies)
    #     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    #     print_vacancies(top_vacancies)
    # else:
    #     print("Не удалось получить вакансии. Пожалуйста, проверьте запрос и попробуйте снова.")


if __name__ == '__main__':
    hh = HH()
    sever = JSONFileSaver('C:/Users/denis.shtepa/bogdan.kozintsov/CodePractice/CW-4_HH_Api/data/vacancies.json')
    hh.load_vacancies('водитель')

    vacancy_objects = []
    for vacancy in hh.vacancies:
        vacancy_objects.append(Vacancy(vacancy["name"],
                                       vacancy["alternate_url"],
                                       vacancy["area"],
                                       vacancy["salary"],
                                       vacancy["salary"]["currency"],
                                       vacancy["employer"]))

    vacancy_dicts = []
    for vacancy_object in vacancy_objects:
        vacancy_dicts.append(vacancy_object.to_dict())

    sever.save(vacancy_dicts)
