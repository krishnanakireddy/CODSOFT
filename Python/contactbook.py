contacts = []

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "address" : address
    }

    contacts.append(contact)
    print("Contact added successfully\n")

def view_contacts():
    print("--- Contact List ---")
    if not contacts:
        print("No Contacts found.\n")
        return
    for index, contact in enumerate(contacts, start=1):
        print(f"{index}. {contact['name']} - {contact['phone']}") 

def search_contact():
    print("\n--- Search Contact ---")
    search = input("Enter name or phone number to search: ").lower()

    found = False
    for contact in contacts:
        if search in contact["name"].lower() or search in contact["phone"]:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True

    if not found:
        print("Contact not found.\n")

def update_contact():
    print("\n--- Update Contact ---")
    name = input("Enter name of contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            print("Leave blank to keep current value.")

            new_phone = input(f"New Phone ({contact['phone']}): ")
            new_email = input(f"New Email ({contact['email']}): ")
            new_address = input(f"New Address ({contact['address']}): ")

            if new_phone:
                contact["phone"] = new_phone
            if new_email:
                contact["email"] = new_email
            if new_address:
                contact["address"] = new_address

            print("Contact updated successfully\n")
            return
        
def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter name of contact to Delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:
            contacts.remove(contact)
            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")

def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contacts")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Exiting... Thank You")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__== "__main__":
    main()