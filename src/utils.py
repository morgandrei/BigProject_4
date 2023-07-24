import datetime
from src.api_classes import HeadHunterAPI, SuperJobAPI
import re


def welcome():
    """Функция приветствия пользователя"""
    print("Вас приветствует программа парсинга сайтов HeadHunter и SuperJob!")
    user_name = input("Давайте познакомимся! Введите ваше имя: ")
    date = datetime.datetime.now()
    if 0 <= date.hour <= 6:
        return f"Доброй ночи, {user_name}"
    elif 7 <= date.hour <= 11:
        return f"Доброе утро, {user_name}"
    elif 12 <= date.hour <= 17:
        return f"Добрый день, {user_name}"
    elif 18 <= date.hour <= 24:
        return f"Добрый вечер, {user_name}"
