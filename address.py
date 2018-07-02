#!./venv/bin/python

# Globals
contacts = []
choice = 1
menu = '''
(1) Add        contact
(2) List       contacts
(3) Delete     contact
(4) Delete all contacts
(0) Exit
'''

def create_contact():
    name = input('Name: ')
    phone = input('Phone number: ')
    email = input('Email: ')
    return {'name': name, 'phone': phone, 'email': email}

def print_contacts(id=False):
    for idx, contact in enumerate(contacts):
        if id: print (f'id: {idx+1}')
        for key, val in contact.items():
            print(f'{key}: {val}')
        print('\n')

while choice != 0:
    print(f'\n{menu}')
    choice = int(input('> '))
    if   choice == 0:
        print('Byee, have a great time')
        exit(0)
    elif choice == 1:
        # TODO: Add contact to database
        contact = create_contact()
        contacts.append(contact)
    elif choice == 2:
        # TODO: Get contacts from database
        print_contacts()
        input()
    elif choice == 3:
        # TODO: Delete contact in database
        print_contacts(id=True)
        id = int(input('id to delete: '))
        contacts.remove(contacts[id-1])
    elif choice == 4:
        # TODO: Delete contacts in database
        contacts.clear()
    else:
        print('Invalid option')
