from functions import load_phonebook, save_phonebook, add_entry, view_phonebook,main_menu,other_function


def main():
    other_function()
    filename = 'phonebook.json'
    phonebook = load_phonebook(filename)
    main_menu(phonebook,filename)





if __name__ == '__main__':
    main()
