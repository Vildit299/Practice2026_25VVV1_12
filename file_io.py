import os
import time

from search import is_ordered, binary_search, standard_search


DATA_FOLDER = "file_test"


def read_table(filename):
    paths = [
        filename,
        os.path.join(DATA_FOLDER, filename)
    ]

    file_path = None

    for path in paths:
        if os.path.exists(path):
            file_path = path
            break

    if file_path is None:
        print("Ошибка: файл не найден.")
        return None

    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            lines = file.readlines()

        table = []

        for line in lines:
            line = line.strip()

            if line == "":
                continue

            parts = line.split(",")

            if len(parts) < 3:
                print("Ошибка: строка таблицы содержит мало данных.")
                return None

            key = int(parts[0].strip())
            surname = parts[1].strip()
            group = parts[2].strip()

            if surname == "" or group == "":
                print("Ошибка: в таблице есть пустые поля.")
                return None

            table.append([key, surname, group])

        return table

    except ValueError:
        print("Ошибка: ключ должен быть целым числом.")
        return None

    except Exception:
        print("Ошибка при чтении файла.")
        return None


def write_table(filename, table):
    try:
        if not os.path.exists(DATA_FOLDER):
            os.mkdir(DATA_FOLDER)

        file_path = os.path.join(DATA_FOLDER, filename)

        with open(file_path, "w", encoding="utf-8") as file:
            for row in table:
                file.write(f"{row[0]},{row[1]},{row[2]}\n")

        print("Файл сохранён:", file_path)

    except Exception:
        print("Ошибка при записи файла.")


def write_results(filename, key, size, index, record, comparisons, search_time, std_index, std_time):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("Результаты поиска в упорядоченной таблице\n")
            file.write(f"Количество записей: {size}\n")
            file.write(f"Искомый ключ: {key}\n\n")

            file.write("Собственная реализация бинарного поиска:\n")
            file.write(f"Индекс: {index}\n")
            file.write(f"Сравнений: {comparisons}\n")
            file.write(f"Время: {search_time:.8f} с\n\n")

            if record is None:
                file.write("Запись не найдена\n\n")
            else:
                file.write("Найдена запись:\n")
                file.write(f"Ключ: {record[0]}\n")
                file.write(f"Фамилия: {record[1]}\n")
                file.write(f"Группа: {record[2]}\n\n")

            file.write("Стандартная функция bisect_left:\n")
            file.write(f"Индекс: {std_index}\n")
            file.write(f"Время: {std_time:.8f} с\n")

    except Exception:
        print("Ошибка при записи результатов.")


def input_int(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Ошибка: введите целое число.")


def search_in_table():
    filename = input("Введите имя исходного CSV-файла: ")
    table = read_table(filename)

    if table is None:
        return

    print("Прочитано записей:", len(table))

    if len(table) == 0:
        print("Ошибка: файл пустой.")
        return

    if not is_ordered(table):
        print("Ошибка: таблица не упорядочена по ключу.")
        return

    key = input_int("Введите ключ поиска: ")

    result_filename = input("Введите имя результирующего файла: ")

    if result_filename == "":
        print("Ошибка: имя результирующего файла не может быть пустым.")
        return

    start = time.perf_counter()
    index, comparisons = binary_search(table, key)
    search_time = time.perf_counter() - start

    start = time.perf_counter()
    std_index = standard_search(table, key)
    std_time = time.perf_counter() - start

    if index == -1:
        record = None
    else:
        record = table[index]

    print("\n=== РЕЗУЛЬТАТЫ ПОИСКА ===")
    print(f"Бинарный поиск: индекс={index}, сравнений={comparisons}, время={search_time:.8f} с")

    if record is None:
        print("Запись не найдена.")
    else:
        print("Найдена запись:")
        print("Ключ:", record[0])
        print("Фамилия:", record[1])
        print("Группа:", record[2])

    print("\nСравнение со стандартной функцией:")
    print(f"bisect_left: индекс={std_index}, время={std_time:.8f} с")

    write_results(result_filename, key, len(table), index, record, comparisons, search_time, std_index, std_time)
    print("\nРезультаты сохранены в файл:", result_filename)
