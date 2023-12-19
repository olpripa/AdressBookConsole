from classes import *
from abc_classes import *


def ab_start():
    phone = '38(095)0835767'
    adr = '58009, м.Чернівці, вул. Головна 277Б'
    adress = Adress(adr)
    print(adress, type(adress))
    ph0 = Phone(phone)
    ph1 = Phone('38098083 6767')
    ph2 = Phone('38098850 3797')
    ph3 = Phone('38099 555 66 88')
    ph4 = Phone('38098850 3797')
    ph5 = Phone('38098850 4797')
    b1 = Birthday('09.11.1979')
    b2 = Birthday('26.03.1984')
    em1 = Email('ol.pripa@gmail.com')
    em2 = Email('ol.pripa@ukr.net')
    print(em1, type(em1))
    # print(b1, b2)
    lph = [ph0, ph1, ph3]
    em = [em1, em2]

    name = Name('Pripa Oleksandr')
    # print(name)
    # print(em)
    # print(ph0)
    r0 = Record('Pripa Oleksandr')
    r0.add_adress(adress)
    r0.addemails(em1)
    r0.addemails(em2)

    # print(type(r0.phones), r0.phones)
    # print(lph)
    r0.addphones(ph5)
    r1 = Record('Pripa Y', phones=[ph2], birthday='06.05.2009')
    # print(r1.daystoBirthday())
    r2 = Record('Pripa A', birthday='06.08.2007')
    r3 = Record('Tania', phones=[ph5])
    # print(r2.daystoBirthday())
    r0.addbirthday('09.11.1979')
    r3.addbirthday('26.03.1984')
    # print(r0.daystoBirthday())
    # print(r3.daystoBirthday())
    # print(r2)

    r1.addphones(ph4)
    r1.addphones(ph5)
    ab = AdressBook()
    ab.add(r0)
    ab.add(r1)
    ab.add(r2)
    ab.add(r3)

    for key in ab:
        cli_of = CLI_interface(str(ab[key]))
        cli_of.get_summary()

    return (ab)


ab_start()
