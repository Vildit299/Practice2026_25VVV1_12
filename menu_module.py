from file_io import search_in_table
from randomarray import generate_table


def main():
    while True:
        print("\n===== МЕНЮ =====")
        print("1 - Сгенерировать упорядоченную таблицу")
        print("2 - Найти запись в упорядоченной таблице")
        print("3 - Выход")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            generate_table()
        elif choice == "2":
            search_in_table()
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: неверный пункт меню.")
