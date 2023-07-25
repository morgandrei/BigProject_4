import os
import time
from abc import ABC, abstractmethod
import requests


class PlatformsAPI(ABC):

    @abstractmethod
    def get_vacancies(self, query):
        pass


class HeadHunterAPI(PlatformsAPI):
    url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы HeadHunter
        """
        vacancies_lst = []
        for page in range(5):
            params = {'per_page': 100,
                      'page': page,
                      'text': query,
                      'search_field': 'name',
                      'order_by': "publication_time",
                      }
            vacancies = requests.get(self.url, params=params).json()
            vacancies_lst.extend(vacancies['items'])
            if (vacancies['pages'] - page) <= 1:
                break
            time.sleep(0.5)
        return vacancies_lst


class SuperJobAPI(PlatformsAPI):
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def __init__(self):
        self.x_api_app_id = os.getenv('X-Api-App-Id')

    def get_vacancies(self, query: str):
        """
        Получение списка вакансий с платформы SuperJob
        """
        vacancies_lst = []
        for page in range(5):

            headers = {
                'X-Api-App-Id': self.x_api_app_id,
            }
            params = {'keyword': query,
                      'page': page,
                      'count': 100,
                      'order_direction': 'desc',
                      }

            vacancies = requests.get(self.url, headers=headers, params=params).json()
            try:
                vacancies_lst.extend(vacancies['objects'])
            except KeyError:
                return print(vacancies['error']['message'])
            else:
                if not vacancies['more']:
                    break
                time.sleep(0.5)
        return vacancies_lst
