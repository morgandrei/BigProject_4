import os
import json
import re
import time
from abc import ABC, abstractmethod
from configparser import ParsingError

import requests


class PlatformsAPI(ABC):

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterAPI(PlatformsAPI):
    url = 'https://api.hh.ru/vacancies'

    def get_vacancies(self, keyword):
        # Справочник для параметров GET-запроса
        params = {
            "text": keyword,  # Ключевое слово для поиска вакансий
            "page": None,
            "per_page": 100,  # Кол-во вакансий на 1 странице
            "archive": False,
        }

        data = requests.get(self.url, params=params).json()  # Посылаем запрос к API

        return json.dumps(data, indent=2, ensure_ascii=False)


class SuperJobAPI(PlatformsAPI):
    url = 'https://api.superjob.ru/2.0/vacancies/'

    def get_vacancies(self, keyword):
        self.params = {
            'keyword': keyword,  # Ключевое слово для поиска вакансий
            'page': None,
            'count': 100,  # Кол-во вакансий на 1 странице
            'archive': False,
        }
        self.headers = {
            'X-Api-App-Id': os.getenv('X-Api-App-Id')
        }
        data = requests.get(self.url, headers=self.headers, params=self.params)
        if data.status_code != 200:
            raise ParsingError(f"Ошибка получения вакансий! Статус: {data.status_code}")
        return json.dumps(data.json()["objects"], indent=2, ensure_ascii=False)


#hh_api = HeadHunterAPI()
#print(hh_api.get_vacancies('python'))
#superjob_api = SuperJobAPI()
# print(superjob_api.get_vacancies('python'))
