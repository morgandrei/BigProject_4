import re

from src.api_classes import HeadHunterAPI, SuperJobAPI
from src.vacancy import Vacancy

hh_api = HeadHunterAPI()
sj_api = SuperJobAPI()


def conv_hh_vacancies(vacancy_list: list) -> list:
    """
    Преобразование результатов запроса в список экземпляров класса Vacancy
    """
    converted_vacancies = []
    for elem in vacancy_list:
        title = elem['name']
        link = elem['alternate_url']
        salary = format_hh_salary(elem['salary'])
        area = elem['area']['name']
        description = f"{elem['snippet']['requirement']}\n{elem['snippet']['responsibility']}"
        clean_description = re.sub('<highlighttext>|</highlighttext>', '', description)
        converted_vacancy = Vacancy(title, link, salary, area, clean_description)
        converted_vacancies.append(converted_vacancy)
    return converted_vacancies


def format_hh_salary(salary: dict | None) -> str:
    """
    Форматирование блока зарплаты и валюты
    """
    if salary is None:
        return "Не указана"
    elif salary['to'] is None:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"от {salary['from']} {currency}"
    elif salary['from'] is None:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"до {salary['to']} {currency}"
    else:
        currency = salary.get('currency')
        if currency == 'RUR':
            currency = 'руб.'
        elif currency == 'BYR':
            currency = 'бел. руб.'
        return f"от {salary['from']} до {salary['to']} {currency}"


def conv_sj_vacancies(vacancy_list: list) -> list:
    """
    Преобразование результатов запроса в список экземпляров класса Vacancy
    """
    converted_vacancies = []
    for elem in vacancy_list:
        title = elem['profession']
        link = elem['link']
        salary_from = elem['payment_from']
        salary_to = elem['payment_to']
        currency = elem.get('currency')
        if currency == 'rub':
            currency = 'руб.'
        elif currency == 'uah':
            currency = 'грн.'
        elif currency == 'uzs':
            currency = 'сум'

        if salary_from == 0 and salary_to == 0:
            salary = "Не указана"
        elif salary_to == 0:
            salary = f"от {salary_from} {currency}"
        elif salary_from == 0:
            salary = f"до {salary_to} {currency}"
        elif salary_from == salary_to:
            salary = f"до {salary_to} {currency}"
        else:
            salary = f"от {salary_from} до {salary_to} руб."
        area = elem['town']['title']
        description = elem['candidat']
        converted_vacancy = Vacancy(title, link, salary, area, description)
        converted_vacancies.append(converted_vacancy)
    return converted_vacancies


def sort_vacancies(vacancies: list) -> list:
    """
    Сортируем вакансии по зарплате
    """
    sorted_vacancies = sorted(vacancies, reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies, top_n):
    """
    олучение указанного топа вакансий
    """
    if top_n > len(vacancies):
        return vacancies[:len(vacancies)]
    else:
        return vacancies[:top_n]


def convert_vacancy(vacancies_list: list) -> list:
    """
    Преобразование списка словарей в экземпляры класса
    """
    converted_list = []
    for vacancy in vacancies_list:
        title = vacancy['title']
        link = vacancy['link']
        salary = vacancy['salary']
        area = vacancy['area']
        description = vacancy['description']
        converted_vacancy = Vacancy(title, link, salary, area, description)
        converted_list.append(converted_vacancy)
    return converted_list


def get_search_query_and_top_n():
    """
    Вывели повторяющиеся запросы в отдельную функцию
    """
    search_query = input('Введите поисковый запрос: ').lower().strip()
    top_n = int(input("Введите количество вакансий для вывода в топ N по зарплате: "))
    filter_word = input(
        "Введите ключевое слово для фильтрации вакансий: ").lower().strip()
    return search_query, top_n, filter_word


def process_vacancies(convert_vacancies, top_n):
    """
    Обработка запросов пользователя, вывод информационных сообщений
    """
    user_sort = input('Отсортировать вакансии по зарплате? Да/Нет\n').lower().strip()
    if user_sort == 'да':
        sorted_vacancies = sort_vacancies(convert_vacancies)
    else:
        sorted_vacancies = convert_vacancies
    user_top = int(input('1 - Вывести топ вакансий\n'
                         '2 - Вывести все\n'))
    if user_top == 1:
        top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
        print(*top_vacancies)
    elif user_top == 2:
        print(*sorted_vacancies)
    else:
        print('Такого варианта нет, вывожу всё')

        print(*sorted_vacancies)