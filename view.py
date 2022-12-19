def contact_to_s():
    return input('Введите информацию для поиска: ')

def choose_mode():
    return input ('Выбереите режим работы: 1 - добавление, 2 - поиск, 3 - выход из справочника ')


def new_contact():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер контакта: ")
    company_name = input("Введите название организации: ")
    return f'{last_name} || {first_name} || {middle_name} || {phone_number} ||| {company_name}'

def show_found (result):
    print ('Результаты поиска: ')
    for i in result:
        print(i)