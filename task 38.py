# Задача 38: Создать телефонный справочник возможностью добавления записей и чтения. 
# Пользователь также может ввести фамилию, тогда программа должны вывести на экран все записи с этой фамилий.
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.

# with open('phone_book.txt', "r", encoding="utf-8") as data:
#         print(data.read())
#         print("")

# def export_data(phone_book):
#     with open(phone_book.txt, "r", encoding="utf-8") as data:
#         tel_file = data.read()
#     num = len(tel_file.split("\n"))
#     with open(phone_book.txt, "a", encoding="utf-8") as data: 
#         fio = input("Введите ФИО: ")
#         phone_number = input("Введите номер телефона: ")
#         data.write(f"{num} | {fio} | {phone_number}\n")
#         print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")

# def edit_data(phone_dook):
#     print("\nПП | ФИО | Телефон")
#     with open(phone_dook.txt, "r", encoding='utf-8') as data:
#         tel_book = data.read()
#     print(tel_book)
#     print("")
#     index_delete_data = int(input("Введите номер строки для редактирования: ")) - 1
#     phone_book_lines = tel_book.split("\n")
#     edit_tel_book_lines = phone_book_lines[index_delete_data]
#     elements = edit_tel_book_lines.split(" | ")
#     fio = input("Введите ФИО: ")
#     phone = input("Введите номер телефона: ")
#     num = elements[0]
#     if len(fio) == 0:
#         fio = elements[1]
#     if len(phone) == 0:
#         phone = elements[2]
#     edited_line = f"{num} | {fio} | {phone}"
#     phone_book_lines[index_delete_data] = edited_line
#     print(f"Запись - {edit_tel_book_lines}, изменена на - {edited_line}\n")
#     with open(filename, "w", encoding='utf-8') as f:
#         f.write("\n".join(phone_book_lines))
# while my_choice != 0:
#         print("Выберите одно из действий:")
#         print("1 - Вывести инфо на экран")
#         print("2 - Произвести экпорт данных")
#         print("3 - Произвести изменение данных")
#         action = int(input("Действие: "))
#         if action == 1:
#             show_data(file_tel)
#         elif action == 2:
#             export_data(file_tel)
#         elif action == 3:
#             edit_data(file_tel)
#         else:
#             my_choice = 0

# print("До свидания")

def show_data(filename):
    print("\033[31m\0")
    print("\n № | Ф.И.О | Телефон")
    with open(filename, "r", encoding="utf-8") as data:
        print(data.read())
    print("")

def export_data(filename):
    print("\033[34m\0")
    with open(filename, "r", encoding="utf-8") as data:
        tel_file = data.read()
    num = len(tel_file.split("\n"))
    with open(filename, "a", encoding="utf-8") as data: 
        fio = input("Введите ФИО: ")
        phone_number = input("Введите номер телефона: ")
        data.write(f"{num} | {fio} | {phone_number}\n")
        print(f"Добавлена запись : {num} | {fio} | {phone_number}\n")

def find_data(filename):
    print("\033[33m\0")
    with open(filename, 'r', encoding='utf-8') as data:
        find = data.read().split('\n')
        temp = input('Кого ищем?: ')
        for i in find:
            if temp in i:
                print(i)

def main():
    my_choice = -1
    file_tel = "tel.txt"

    with open(file_tel, "a", encoding="utf-8") as file:
         file.write('')

    while my_choice != 0:
        print("\033[32m\0")
        print("Выберите одно из действий:")
        print("1 - Вывести инфо на экран")
        print("2 - Произвести экспорт данных")
        print("3 - Поиск ")
        print("0 - Выход из программы")
        action = int(input("Действие: "))
        if action == 1:
            show_data(file_tel)
        elif action == 2:
            export_data(file_tel)
        elif action == 3:
            find_data(file_tel)
        else:
            my_choice = 0

    print("До свидания")

if __name__ == "__main__":
    main()