#Step 1: Define the Contact Class
python
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

#Step 2: Define the ContactList Class
python
import json

class ContactList:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, 'r') as file:
                return [Contact(**data) for data in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump([vars(contact) for contact in self.contacts], file)

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        self.save_contacts()

#Step 3: Create the User Interface
python
def main():
    contact_list = ContactList()

    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            new_contact = Contact(name, phone, email)
            contact_list.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == '2':
            print("\nContacts:")
            contact_list.view_contacts()

        elif choice == '3':
            name = input("Enter the name of the contact to delete: ")
            contact_list.delete_contact(name)
            print(f"Contact '{name}' deleted successfully!")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()