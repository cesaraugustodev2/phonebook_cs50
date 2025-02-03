# Contact Book - Patient Management

This project is a simple contact book application for managing patient information, such as name, phone number, email, prescribed medications, and diseases. The data is stored in a JSON file, ensuring persistence and ease of manipulation.

## Features

- **Add Patient**: Enter a new patient with detailed information.
- **View Contact Book**: Display all registered patients in the contact book.
- **Delete Patient**: Remove a specific patient from the contact book.
- **Data Persistence**: Data is stored in a JSON file to ensure information is retained between sessions.

## Project Structure

The project is divided into the following files:

1. **main.py**: The main file that starts the program and calls the necessary functions.
2. **functions.py**: Contains all the functions that implement the application's logic.
3. **phonebook.json**: A JSON file used to store contact book data.

### Description of Files

#### 1. `main.py`

This file is responsible for initializing the application and loading the contact book data. It calls the main function `main_menu` to display the interactive menu to the user.

#### 2. `functions.py`

Contains the following main functions:

- **`load_phonebook(filename)`**: Loads the contact book data from the JSON file. If the file does not exist, it returns an empty contact book.
- **`save_phonebook(phonebook, filename)`**: Saves the contact book data to the JSON file.
- **`add_entry(phonebook, filename)`**: Allows adding a new patient to the contact book.
- **`del_entry(phonebook, filename)`**: Removes an existing patient from the contact book.
- **`view_phonebook(phonebook)`**: Displays all entries in the contact book in the terminal.
- **`main_menu(phonebook, filename)`**: Presents the main menu with interactive options for the user.

#### 3. `phonebook.json`

This file stores patient data in JSON format. An example of the file structure is shown below:

```json
{
    "yulia": {
        "name": "Yulia",
        "phone": "+1-456-345-123",
        "email": "yulia@harvard.com",
        "medicine": "Vitamin D",
        "disease": "tuberculosis"
    },
    "maria": {
        "name": "Maria",
        "phone": "+1-345-654-752",
        "email": "maria@harvard.com",
        "medicine": "Amoxillin",
        "disease": "pneumonia"
    }
}
```

### Data Structure

Each entry in the JSON file follows this format:

```json
"patient_name": {
    "name": "Patient Name",
    "phone": "Phone Number",
    "email": "Email Address",
    "medicine": "Prescribed Medication",
    "disease": "Diagnosed Disease"
}
```

### Example Entry

```json
{
    "david": {
        "name": "David",
        "phone": "+1-345-456-789",
        "email": "david@harvard.com",
        "medicine": "Diazepan",
        "disease": "Depression"
    }
}
```

## How to Use

1. Make sure you have Python installed on your machine.
2. Clone this repository or copy the necessary files.
3. Run the program with the command:

   ```bash
   python main.py
   ```

4. Follow the instructions displayed in the interactive menu:
   - Press `A` to add a new patient.
   - Press `V` to view the list of patients.
   - Press `D` to delete an existing patient.
   - Press `Q` to exit the program.

## Prerequisites

- Python 3.x
- Standard library `json` (already included in Python)

## Interactive Menu Structure

The main menu presents the following options:

```
A to add a new entry
V to view phonebook
D to delete an entry
Q to quit
```

## Example Usage

### Add Patient

When selecting option `A`, you will be prompted to enter the following information:

1. Patient's name
2. Phone number
3. Email address
4. Prescribed medication
5. Diagnosed disease

After entering these details, they will be automatically saved to the JSON file.

### View Contact Book

When selecting option `V`, all registered patients will be displayed in the following format:

```
Name       Phone            Email                Medication      Disease
Yulia      +1-456-345-123   yulia@harvard.com    Vitamin D       Tuberculosis
Maria      +1-345-654-752   maria@harvard.com    Amoxillin       Pneumonia
```

### Delete Patient

When selecting option `D`, you will be prompted to enter the name of the patient you wish to delete. The program will confirm before performing the deletion.

## Creating Initial Data (Optional)

If you want to create an initial contact book with some examples, use the following Python code:

```python
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
        "disease":"Tuberculosis"
    },
    'Maria': {
        "name": "Maria",
        "phone": "+1-345-654-752",
        "email": "maria@harvard.com",
        "medicine": "Amoxillin",
        "disease":"Pneumonia"
    }
}

with open('phonebook.json', 'w') as file:
    json.dump(phonebook, file, indent=4)
```

Run this code to create a `phonebook.json` file with initial examples.

## Contribution

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is distributed under the MIT License. See the LICENSE file for more details.

