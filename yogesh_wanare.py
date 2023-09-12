class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class ContactList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully!")

    def search_contact(self, search_name):
        for contact in self.contacts:
            if contact.name.lower() == search_name.lower():
                print("Contact found:")
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                return
        print(f"Contact with name '{search_name}' not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print("-" * 20)
        else:
            print("Contact list is empty.")

def main():
    my_contact_list = ContactList()

    while True:
        print("\nContact List Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Contacts")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            new_contact = Contact(name, phone_number, email)
            my_contact_list.add_contact(new_contact)

        elif choice == "2":
            search_name = input("Enter name to search: ")
            my_contact_list.search_contact(search_name)

        elif choice == "3":
            my_contact_list.display_contacts()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

