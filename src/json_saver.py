
from abc import ABC, abstractmethod



class AbstractVacancyDatabase(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_keyword(self, keyword):
        pass

    @abstractmethod
    def remove_vacancy(self, vacancy_id):
        pass

