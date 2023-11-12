# -*- coding: utf-8 -*-
""""Console module Adress_Book
    
    A simple console module for working with the AdressBook
    AdressBook --> Name, Phone, E-mail
    
    Functions:
        add Name, phone1, phone2, ..., phoneN: add new user to AdressBook: Name, *Phone
        load: зчитає з файлу останню збережену адресну книгу
        phoneadd Name, phone1, phone2, ..., phoneN: add new phone to existing User in AdressBook
        phonechange Name, phone, newphone: change for existing user (name), phone to newphone
        phonedel Name, phone: delete phone from list of phone for existing user (name).
        phone Name: show for existing user (name) list of phone. 
        show: print to console all items of AdressBook
        save: збереже поточну адресну книгу у файл, при завершенні роботи спрацьовує автоматично
        search Str_search: show
        hello: output info about script
        . or exit or goodbye or close: exit from script

"""
from classes import *
import pickle


class MoreArgument(Exception):
    pass


dict_users_phone = AdressBook()


def input_error(func):
    # decorator
    def inner(*arg):
        try:
            result = func(*arg)
            return result
        except KeyError:
            return "User not exist"
        except ValueError:
            return 'Give me name and phone please'
        except IndexError:
            return 'Enter user name'
        except TypeError:
            return 'Arguments is more Type'
        except MoreArgument:
            return 'Arguments is more'
    return inner


def hello():
    # outputs to the console on hello
    print(__doc__)
    return f"How can I help you?"


# @input_error
def user_add(name, phones=[]):
    """
    Add a new contact to the AdressBook
    add UserName phone1, phone2, ... phoneN
    """
    if name in dict_users_phone.keys():
        return f'User {name} - exist with phone number {dict_users_phone.get(name).showphones()}'
    else:
        r = Record(name)
        dict_users_phone.add(r)
        if phones:
            phone_add(name, phones)
        return f'add to list {name}, {phones}'


# @input_error
def phone_add(name, phones=[]):
    # the new phone number of an existing contact
    if name in dict_users_phone.keys():
        for ph in phones:
            try:
                phone = Phone(ph)
                print(dict_users_phone.get(name).addphones(phone))
            except ValueError:
                return f'Check phone nubmer {ph}'

        return 'add phones completed'  # f'add for {name} phones: {phones}'
    else:
        return f'and user {name} not exist'


def phone_change(name, phones=[]):
    # the new phone number of an existing contact
    if name in dict_users_phone.keys():
        return dict_users_phone.get(name).editphone(
            Phone(phones[0]), Phone(phones[1]))
    else:
        return f'and user {name} not exist'


@input_error
def phone_del(name, phone):
    # the new phone number of an existing contact
    if name in dict_users_phone.keys():
        return dict_users_phone.get(name).delphone(Phone(phone[0]))
    else:
        return f'user {name} not exist'


@input_error
def phone_show(name):
    # show("username") outputs the phone number for the specified contact to the console.
    if name in dict_users_phone.keys():
        return f'User {name} - have phone number {dict_users_phone.get(name).showphones()}'
    else:
        return f'and user {name} not exist'


@input_error
def birthday_add(name, birthday):

    if name in dict_users_phone.keys():
        return dict_users_phone.get(name).addbirthday(birthday[0].strip(' '))


@input_error
def adress_add(name, adress):
    if name in dict_users_phone.keys():

        return f'add for {name} adress {adress}'
    else:
        return f'and user {name} not exist'


@input_error
def show_all():
    # outputs all phone number in list to the console.
    page = Paginator(dict_users_phone)
    for p in page:
        result = ''
        for key in p:
            result += f'{str(dict_users_phone[key])}\n'
        print(result)
        if input('Pres Enter'):
            continue
    return f'Done'


@input_error
def search(str_search):
    if len(str_search) < 3:
        return f'minimum number of characters to search is 3'
    else:
        result = ''
        for key in dict_users_phone.search(str_search):
            result += f'{str(dict_users_phone[key])}\n'
        print(result)
        return f'Search {str_search}'


@input_error
def load():
    with open(data_file, "rb") as file:
        print(len(pickle.load(file)))
        if len(pickle.load(file)) > 0:
            return pickle.load(file)
        else:
            return False


@input_error
def exit():
    with open(data_file, "wb") as file:
        pickle.dump(dict_users_phone, file)
    print("Good bye!")
    return


data_file = 'data.bin'

dict_commands = {"hello": hello,
                 "add": user_add,
                 "phoneadd": phone_add,
                 "phonedel": phone_del,
                 "phonechange": phone_change,
                 "phone": phone_show,
                 "addbirthday": birthday_add,
                 "addadress": adress_add,
                 "deladress": adress_add,
                 "show": show_all,
                 "search": search,
                 "exit": exit,
                 "goodbye": exit,
                 "close": exit,
                 ".": exit,
                 }


def action(func,  dictionary,  default="Command not exist"):
    if func in dictionary:
        return dictionary[func]
    return lambda * x:  default


def parser_arg(text: str):
    data = text.strip().split(',')
    if len(data) > 1:
        name = data.pop(0)
        t = name, data
    else:
        t = data[0],
    return t


def main():

    global dict_users_phone

    dict_users_phone = load()
    arg = ''
    print(f'main-code в {__name__} виконується тут\n {__doc__}')
    try:
        while True:
            command, *arg = input('>>>').strip().split(' ', 1)
            if arg:
                arg = parser_arg(''.join(arg))

            do = action(command, dict_commands)
            result = do(*arg)
            if not result:
                break
            print(result)

    except KeyboardInterrupt:
        exit()

        # print("Good bye!")


if __name__ == "__main__":
    main()
