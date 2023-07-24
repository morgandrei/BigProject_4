class Vacancy:

    def __init__(self, title: str, link: str, salary: str, area: str, description: str) -> None:
        try:
            self.__check(title, link, salary, area, description)
        except ValueError as message:
            print(message)
        else:
            self.__title = title
            self.__link = link
            self.__salary = salary
            self.__area = area
            self.__description = description

    def __str__(self):
        return f'\nВакансия: {self.__title} ' \
               f'Ссылка на вакансию: {self.__link}\n' \
               f'Зарплата: {self.__salary} ' \
               f'Город: {self.__area}\n' \
               f'Описание: {self.__description}\n'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__title}, {self.__link}, ' \
               f'{self.__salary}, {self.__area}, {self.__description})'

    @property
    def title(self):
        return self.__title

    @property
    def link(self):
        return self.__link

    @property
    def salary(self):
        return self.__salary

    @property
    def area(self):
        return self.__area

    @property
    def description(self):
        return self.__description

    @staticmethod
    def __check(title, link, salary, area, description):
        """Проверка на валидность данных"""
        if not isinstance(title, str) or len(title.strip()) == 0:
            raise ValueError('Название вакансии должно быть непустой строкой')
        if not isinstance(link, str) or len(link.strip()) == 0:
            raise ValueError('Ссылка на вакансию должна быть непустой строкой')
        if not isinstance(salary, str):
            raise ValueError('Зарплата должна быть строкой')
        if not isinstance(area, str) or len(area.strip()) == 0:
            raise ValueError('Название города должно быть непустой строкой')
        if not isinstance(description, str) or len(description.strip()) == 0:
            raise ValueError('Описание вакансии должно быть непустой строкой')

    @staticmethod
    def convert_salary(self_sal: str, other_sal: str) -> tuple:
        """
        Конвертируем зарплату для возможности сравнения
        :param self_sal: str
        :param other_sal: str
        :return: tuple
        """
        # Разбиваем зарплату на отдельные элементы
        self_salary_list = [i for i in self_sal.split() if i.isdigit()]
        other_salary_list = [i for i in other_sal.split() if i.isdigit()]

        # Проверяем зарплаты на наличие, если не указана то приравниваем 0
        # сравниваем по минимальной границе зарплаты
        if not self_salary_list:
            self_salary = 0
        else:
            self_salary = int(self_salary_list[0])
        if not other_salary_list:
            other_salary = 0
        else:
            other_salary = int(other_salary_list[0])
        return self_salary, other_salary

    def __eq__(self, other):
        self_salary, other_salary = self.convert_salary(self.salary, other.salary)
        return self_salary == other_salary

    def __gt__(self, other):
        self_salary, other_salary = self.convert_salary(self.salary, other.salary)
        return self_salary > other_salary

    def __lt__(self, other):
        self_salary, other_salary = self.convert_salary(self.salary, other.salary)
        return self_salary < other_salary