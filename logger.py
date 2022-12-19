import csv

def add_new(contact):
    try:
        with open('phone_book.txt', 'a', encoding='utf-8') as book:
            book.write(f'\n{contact}')
        with open('phone_book.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])
    except FileNotFoundError:
        with open('phone_book.txt', 'w', encoding='utf-8') as book:
            book.write(f'{contact}')
        with open('phone_book.csv', 'w') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerows([contact.split(' || ')])

def get_base():
    with open('phone_book.txt', 'r', encoding='utf-8') as book:
        return book.read()