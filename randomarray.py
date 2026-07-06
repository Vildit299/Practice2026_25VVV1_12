import random

from file_io import write_table


def input_int(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Ошибка: введите целое число.")


def make_random_ordered_table(size, min_key, max_key):
    surnames = [
        "Иванов",
        "Петров",
        "Сидоров",
        "Смирнов",
        "Козлов",
        "Волков",
        "Орлов",
        "Соколов",
        "Морозов",
        "Федоров"
    ]

    groups = [
        "25ВВВ1",
        "25ВВВ2",
        "25ВВВ3"
    ]

    if max_key - min_key + 1 < size:
        return None

    keys = []
    previous_key = min_key - 1

    for i in range(size):
        remaining = size - i - 1
        max_allowed = max_key - remaining
        key = random.randint(previous_key + 1, max_allowed)
        keys.append(key)
        previous_key = key

    table = []

    for i in range(size):
        surname = surnames[i % len(surnames)]
        group = groups[i % len(groups)]
        table.append([keys[i], surname, group])

    return table


def generate_table():
    size = input_int("Введите количество записей таблицы: ")
    min_key = input_int("Введите минимальный ключ: ")
    max_key = input_int("Введите максимальный ключ: ")

    if size <= 0:
        print("Ошибка: количество записей должно быть больше нуля.")
        return

    if min_key > max_key:
        print("Ошибка: минимальный ключ не может быть больше максимального.")
        return

    table = make_random_ordered_table(size, min_key, max_key)

    if table is None:
        print("Ошибка: диапазон ключей слишком маленький для указанного количества записей.")
        return

    filename = input("Введите имя CSV-файла для сохранения: ")

    if filename == "":
        print("Ошибка: имя файла не может быть пустым.")
        return

    write_table(filename, table)
