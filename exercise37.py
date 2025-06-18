contacts = {}

def add_contact(name, phone):
    contacts[name] = phone

def search_contact(name):
    return contacts.get(name, "Contact not found.")

def show_contacts():
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

# Example usage
add_contact("Alya", "0501234567")
add_contact("Fatima", "0507654321")

print(search_contact("Alya"))
print("All Contacts:")
show_contacts()
