from prompt_toolkit.completion import WordCompleter
from prompt_toolkit import prompt
from prompt_toolkit.shortcuts import radiolist_dialog


def show_menu():
    return radiolist_dialog(
        title="Choose action",
        text="What would you like to do ?",
        values=[
            ("phonebook", "Phone book"),
            ("notebook", "Notebook"),
            ("sort", "Sort directory"),
        ]
    ).run()


def get_user_input():
    menu_completer = WordCompleter(
        ['add', 'add_b', 'add_phone', 'change', 'days_to_birthday', 'birthday',
         'find', 'hello', 'help', 'show_all',
         'exit', 'close', 'good_bye'], ignore_case=True, WORD=True, match_middle=True)
    return prompt("Enter user name and phone number or 'help' for help: ", completer=menu_completer)


def main():
    menu_result = show_menu()
    print(menu_result)
    if menu_result == "phonebook":
        user_input = get_user_input()
        print('You said: %s' % user_input)


if __name__ == "__main__":
    main()
