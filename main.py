from functions import load_phonebook, save_phonebook, add_entry, view_phonebook,main_menu


def main():
    filename = 'phonebook.json'
    phonebook = load_phonebook(filename)
    main_menu(phonebook,filename)
    other_function()




if __name__ == '__main__':
    main()
