# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления 
# данных. Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных.

import os, sys

def main_read_contacts():
    phonebook = dict()
    with open('phonebook.txt', 'r', encoding='utf-8') as data:
        s = data.readlines()
        for i in range(len(s)):
            phonebook[i] = s[i].split()
        # print(phonebook)

# def read_contact(some_line):
#     # found_contacts = list()
#     # with open('phonebook.txt', 'a+', encoding='utf-8') as data:
#     #     for i in data:
#     #         if s in i.split:
#     #             found_contacts.append(s)
#     # return found_contacts


def write_contact(new_contact):
    with open('phonebook.txt', 'a+', encoding='utf-8') as data:
        data.writelines(' '.join(new_contact) + '\n')
        phonebook[len(phonebook) + 1] = new_contact

def input_contact():
    new_contact = list()
    new_contact.append(input('Surname: '))
    new_contact.append(input('Name: '))
    new_contact.append(input('Paternal name: '))
    new_contact.append(input('Phone: '))
    write_contact(new_contact)

def find_contact():
    some_line = input('Who do you want to find? ')
    pb = open('phonebook.txt', 'r')
    found_contacts = list()
    for line in pb:
        if some_line in line:
            found_contacts.append(line)
    pb.close()
    print(found_contacts)

def delete_entry(new_line):
    with open('phonebook.txt', 'r') as rpb:
        lines = rpb.readlines()
        with open('phonebook.txt', 'w') as wpb:
            for line in lines:
                if new_line not in line:
                    wpb.write(line)
    print('Deleted')

def edit_entry(new_edit):
    with open('phonebook.txt', 'r') as rpb:
        lines = rpb.readlines()
        with open('phonebook.txt', 'w') as wpb:
            for line in lines:
                if new_edit in line:
                    line = line.split()
                    for part in line:
                        new_info = part.replace(part, input(f'Write new info instead of {part}: '))
                        wpb.writelines(new_info + ' ')
                    print('Done.')
                else:
                    print('Not found.')
            

def user_interface():
    main_read_contacts()
    print('Phonebook\nWhat do you want?\n1 - Add contact\n2 - Find contact\n3 - Show the whole phonebook\n4 - Delete any entry\n5 - Edit any entry\n0 - Quit programme')
    user_input = input('Your choice: ')
    # while user_input in ('1', '2', '3'):
    if user_input == '1':
        input_contact()
    elif user_input == '2':
        find_contact()
    elif user_input == '3':
        print(phonebook)
    elif user_input == '4':
        new_line = input('What would you like to delete? ')
        delete_entry(new_line)
    elif user_input == '5':
        new_edit = input('What would you like to edit? ')
        edit_entry(new_edit)
    elif user_input == '0':
        print('Okay, bye!')


phonebook = dict()
user_interface()

