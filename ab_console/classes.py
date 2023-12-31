from collections import UserDict
from collections.abc import Iterator
from pathlib import Path
from typing import Any
from country_phone_dict import country_phone_dict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value):
        self.__value = None
        self.value = value

    def __str__(self) -> str:
        if self.value == None:
            return f''
        else:
            return self.value

    def __repr__(self) -> str:
        return self.value


class Name(Field):
    ...


class Phone(Field):

    def __init__(self, value):
        # super().__init__(value)
        self.__phone = value
        self.phone = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    # 1. Sanitize phone
    # 2. Check phone is digits
    # 3. Chek country cod and lenth
    def phone(self, value: str):
        value = self.__sanitize(value)
        # лічильник, який збільшиться, якщо введений номер введений в правильному форматі (код країни, номер)
        count = 0
        if value.isdigit():
            for cod in country_phone_dict:
                if value.startswith(cod):

                    if len(value) == country_phone_dict[cod][1]:
                        self.__phone = value
                        count = 1
                        continue
                    else:
                        error = 'for {}, the phone number must be long {}'.format(
                            country_phone_dict[cod][0], country_phone_dict[cod][1])
                        if not error:
                            print(error)
                        raise ValueError(error)
            if count == 0:
                raise ValueError('Phone not have country cod')

        else:
            print('Phone number is not digit')
            raise ValueError('Phone number is not digit')

    def __eq__(self, other):
        if hasattr(other, 'phone'):
            return self.phone == other.phone
        return self.value == other

    def __str__(self) -> str:
        return self.phone

    def __repr__(self) -> str:
        return self.phone

    @classmethod
    def __sanitize(cls, phone):
        phone = (
            phone.strip()
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace("+", "")
            .replace(" ", "")
        )
        return phone


class Email(Field):
    ...


class Adress(Field):
    ...


class Birthday(Field):

    def __init__(self, value) -> None:
        self.__birthday = value
        self.birthday = value

    def __str__(self) -> str:
        return str(self.__birthday)

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value: str):
        try:
            self.__birthday = datetime.strptime(value, '%d.%m.%Y').date()
        except ValueError:
            print("Format Birthday must be: dd.mm.yyyy")
            return ValueError("Format Birthday must be: dd.mm.yyyy")


class Record(Field):

    def __init__(self, value, phones=None, emails: Email = None, adress: Adress = None, birthday: Birthday = None):

        self.name = Name(value)
        self.phones: list = phones
        self.emails: list = emails
        self.adress = adress
        if birthday:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def __str__(self) -> str:
        ph = '\nPhones: ' + ", ".join(str(p)
                                      for p in self.phones) if self.phones else ""
        em = '\nE-mail: ' + ", ".join(str(e)
                                      for e in self.emails) if self.emails else ''
        return '{:-^50}'.format('Contact') + '\n' + '{0:<25} {4:10} {1} {2} {3} {5}'.format(str(self.name), ph, em,
                                                                                            "\nAdres: " + (str(self.adress)) if self.adress != None else "", str(self.birthday), "\n")

    def showphones(self):
        if self.phones:
            return 'Phones: {}'.format(", ".join(str(p) for p in self.phones))
        else:
            return ''

    def showemails(self):
        if self.emails:
            return 'E-mails: {}'.format(", ".join(str(e) for e in self.emails))
        else:
            return ''

    def addphones(self, *phones):  # phone --> object class Phone
        # function  add Phones from Phone list of User
        if not self.phones:
            self.phones = [*phones]
        else:
            for phone in phones:
                if phone in self.phones:
                    return '{} already exiting phone: {}'.format(self.name, phone)
                else:
                    self.phones.append(phone)
                    return 'To list of {} add Phone: {}'.format(self.name, phone)

    def addemails(self, *emails):  # phone --> object class Phone
        # function  add Phones from Phone list of User
        if not self.emails:
            self.emails = [*emails]
        else:
            for email in emails:
                if email in self.emails:
                    return '{} already exiting phone: {}'.format(self.name, email)
                else:
                    self.emails.append(email)
                    return 'To list of {} add Email: {}'.format(self.name, email)

    def delphone(self, phone: Phone):  # phone --> object class Phone
        # function  delete Phone from Phone list of User

        if phone in self.phones:
            return 'from list of {} delete phone: {}'.format(self.name,
                                                             self.phones.pop(self.phones.index(phone, 0)))
        else:
            return '{} not have phone: {}'.format(self.name, phone)

    # function edit Phone from Phone list of User
    def editphone(self, phone: Phone, new_phone: Phone):  # phone --> object class Phone

        if phone in self.phones:
            self.phones.insert(self.phones.index(phone, 0)+1, new_phone)
            return 'in list of {} Phone: {} change to {}'.format(self.name,
                                                                 self.phones.pop(
                                                                     self.phones.index(phone, 0)),
                                                                 new_phone)
        else:
            return '{} not have phone: {}'.format(self.name, phone)

    def add_adress(self, adres: Adress):
        if not self.adress:
            self.adress = adres

    def remove_adress(self):
        self.adress = None

    def daystoBirthday(self):
        if self.birthday:
            today = datetime.today()
            bd = datetime(year=today.year, month=self.birthday.birthday.month,
                          day=self.birthday.birthday.day)
            if bd < today:
                bd = bd.replace(year=today.year + 1)

            time_to_birthday = abs(bd - today)

            return (f'!!!! {time_to_birthday.days}')

    def addbirthday(self, birthday):
        if self.birthday == None:
            self.birthday = Birthday(birthday)
            return 'To list of {} add: {}'.format(self.name, birthday)


class AdressBook(UserDict):

    def __iter__(self) -> Iterator:
        return iter(self.data)

    def add(self, record: Record):
        self.update({record.name.value: record})  # .name

    def search(self, search_str: str):
        keys = []
        if search_str.isdigit():
            print('Search Phone and Name')
            for key, record in self.items():
                if str(record.name).find(search_str) >= 0 or record.showphones().find(search_str.lower()) >= 0:
                    keys.append(key)
            return keys

        else:
            print('Search Name')
            for key, record in self.items():
                if str(record.name).lower().find(search_str.lower()) >= 0:
                    keys.append(key)
            return keys


class Paginator:
    def __init__(self, iterable, page_len=3):
        self.iterable = iterable
        self.page_len = page_len

    def __iter__(self):
        page = []
        for i in self.iterable:
            page.append(i)
            if len(page) == self.page_len:
                yield page
                page = []
        if page:
            yield page
