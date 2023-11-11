from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt

from prompt_toolkit.shortcuts import radiolist_dialog

result = radiolist_dialog(
    title="Choose action",
    text="What would you like to do ?",
    values=[
        ("phonebook", "Phone book"),
        ("notebook", "Notebook"),
        ("sort", "Sort directory"),
    ]
).run()
print(result)

menu_completer = WordCompleter(
    ['add', 'add_b', 'add_phone', 'change', 'days_to_birthday', 'birthday',
     'find', 'hello', 'help', 'show_all',
     'exit', 'close', 'good_bye'], ignore_case=True, WORD=True, match_middle=True)
text = prompt("Enter user name and phone number or 'help' for help: ",
              completer=menu_completer)
print('You said: %s' % text)
