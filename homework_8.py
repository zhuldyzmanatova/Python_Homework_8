def show_menu():
    print('\nВыберите необходимое действие:\n'
          '1. Отобразить весь справочник\n'
          '2. Найти абонента по фамилии\n'
          '3. Изменить номер телефона абонента\n'
          '4. Удалить абонента по фамилии\n'
          '5. Найти абонента по номеру телефона\n'
          '6. Добавить абонента в справочник\n'
          '7. Копировать данные из одного файла в другой\n'
          '8. Сохранить справочник в текстовом формате и закончить работу')
    choice = int(input())
    return choice

 
def work_with_phonebook():
    phone_book = read_txt('phonebook.txt')
    while True:
        choice = show_menu()
        if choice == 8:
            write_txt('phonebook.txt', phone_book)
            break
        elif choice == 1:
            print_result(phone_book)
        elif choice == 2:
            last_name = input('Введите фамилию абонента: ')
            print(find_by_lastname(phone_book, last_name))
        elif choice == 3:
            last_name = input('Введите фамилию абонента: ')
            new_number = input('Введите новый номер: ')
            print(change_number(phone_book, last_name, new_number))
        elif choice == 4:
            last_name = input('Введите фамилию абонента: ')
            print(delete_by_lastname(phone_book, last_name))
        elif choice == 5:
            number = input('Введите номер: ')
            print(find_by_number(phone_book, number))
        elif choice == 6:
            user_data = input('Введите информацию по новому абоненту (фамилия, имя, телефон, описание) через запятую: ')
            result = add_user(phone_book, user_data)
            print(result)
        elif choice == 7:
            source_filename = input('Введите имя файла, откуда скопировать данные: ')
            destination_filename = input('Введите имя файла, куда скопировать данные: ')
            line_number = int(input('Введите номер строки для копирования: '))
            copy_record(source_filename, destination_filename, line_number)


def print_result(phone_book):
    if not phone_book:
        print('Нет данных')
        return
    for record in phone_book:
        print(record)

def find_by_lastname(phone_book, last_name):
    result_for_last_name = []
    for record in phone_book: 
        if record['Фамилия'] == last_name:
            result_for_last_name.append(record)
    if len(result_for_last_name) > 0:
        return result_for_last_name 
    return 'Абонент не существует'


def change_number(phone_book, last_name, new_number):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            record['Телефон'] = new_number
            return 'Номер изменен'
    return 'Абонент не существует'


def delete_by_lastname(phone_book, last_name):
    for record in phone_book:
        if record['Фамилия'] == last_name:
            phone_book.remove(record)
            return 'Абонент удален'
    return 'Абонент не существует'


def find_by_number(phone_book, number):
    result_for_number = []
    for record in phone_book:
        if record['Телефон'] == number:
            result_for_number.append(record)
    if len(result_for_number) > 0:  
        return result_for_number 
    return 'Абонент не существует'


def add_user(phone_book, user_data):
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    user_data = user_data.split(', ')
    if len(user_data) != len(fields):
        return 'Ошибка! Проверьте, вся ли введена информация? (фамилия, имя, телефон, описание)'
    new_record = dict(zip(fields, user_data))
    phone_book.append(new_record)
    return 'Добавлен новый абонент'


def copy_record(source_filename, destination_filename, line_number): # функция то работает, то нет, файл обновляется с опозданием
    with open(source_filename, 'r', encoding='utf-8') as source_file:
        lines = source_file.readlines()
        if line_number > len(lines):
            print('Строка не существует')
            return
        with open(destination_filename, 'a', encoding='utf-8') as destination_file:
            line = lines[line_number - 1]
            print(f'Копируемая строка - {line}')
            destination_file.write(line)
            print('Данные скопированы')


def read_txt(filename):
    phone_book = []
    fields = ['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename, 'r', encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(', ')))
            phone_book.append(record)
    return phone_book


def write_txt(filename, phone_book):
    with open(filename, 'w', encoding='utf-8') as phout:
        for record in phone_book:
            phout.write(', '.join(record[field] for field in record) + '\n')


work_with_phonebook()
