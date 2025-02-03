import json

phonebook = {
    'David': {
        "name": "David",
        "phone": "+1-345-456-789",
        "email": "david@harvard.com",
        "medicine": "Diazepan",
        "disease":"Depression"

    },
    'Yulia': {
        "name": "Yulia",
        "phone": "+1-456-345-123",
        "email": "yulia@harvard.com",
        "medicine": "Vitamin D",
        "disease":"tuberculosis"
    },
    'Maria': {
        "name": "Maria",
        "phone": "+1-345-654-752",
        "email": "maria@harvard.com",
        "medicine": "Amoxillin",
        "disease":"pneumonia"
    }
}

with open('phonebook.json', 'w') as file:
    json.dump(phonebook, file, indent=4)
