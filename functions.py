import json
import os

def load_phonebook(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return {key.lower(): value for key, value in data.items()}
    return {}

def save_phonebook(phonebook, filename):
    with open(filename, 'w') as file:
        json.dump(phonebook, file, indent=4)

def add_entry(phonebook, filename):
    while True:
        new_entry = input("Enter a New patient name: ").capitalize()
        new_phone = input("Enter phone number: ")
        new_email = input("Enter email address: ")
        new_medicine = input("Enter medicine name: ")
        new_disease = input("Enter disease name: ")
        phonebook[new_entry] = {"name": new_entry, "phone": new_phone, "email": new_email,"medicine":new_medicine,"disease":new_disease}
        save_phonebook(phonebook, filename)
        n = input("Do you want to insert another patient? (y/n): ")
        if n.lower() not in ("y", "yes"):
            print("Phonebook Closed!")
            break

def del_entry(phonebook, filename):
    if len(phonebook)==0:
        print("phonebook empty")
    else:
        while True:
            o = input("Enter the patient name to delete: ").lower()
            if o in phonebook:
                c = input(f"Are you sure you want to delete the patient {o}? (y/n): ")
                if c.lower() == "y":
                    print(f"{o} was deleted from phonebook")
                    del phonebook[o]
                    save_phonebook(phonebook, filename)
                    break
                else:
                    print("Ok! No changes made.")
                    break
            else:
                print("Name not Found! Please try again.")




def view_phonebook(phonebook):
    if len(phonebook)==0:
        print("phonebook empty")
    else:
     for value in phonebook.values():
        print(f"{value['name']} \t {value['phone']} \t {value['email']} \t {value['medicine']} \t {value['disease']}")

def main_menu(phonebook, filename):
    while True:
        print("Select an option:")
        o = input("A to add a new entry\nV to view phonebook\nD to delete an entry\nQ to quit\n")
        if o.lower() == "a":
            add_entry(phonebook, filename)
        elif o.lower() == "v":
            view_phonebook(phonebook)
        elif o.lower() == "d":
            del_entry(phonebook, filename)
        elif o.lower() == "q":
            print("Exiting the phonebook.")
            break
        else:
            print("Invalid Option. Try Again!")

def other_function():
    print("Other Function Executed!")
