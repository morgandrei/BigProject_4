from src.utils import welcome

print(welcome())
while True:
    origin_vac = input("Укажите источник поиска вакансий\n1 - hh.ru\n2 - superjob.ru\n3 - оба источника\n0 - завершить программу")

    if origin_vac == '0':
        exit("До свидания!")

    elif origin_vac == '1':
        print("Вы выбрали hh.ru в качестве источника поиска вакансий")

        break
    elif origin_vac == '2':
        print("Вы выбрали superjob.ru в качестве источника поиска вакансий")

        break
    elif origin_vac == '3':
        print("Вы выбрали hh.ru и superjob.ru в качестве источников поиска вакансий")

        break
    else:
        print("Необходимо выбрать действие")

