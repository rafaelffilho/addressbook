#!./venv/bin/python
menu = '''
(1) Add        contact
(2) List       contacts
(3) Delete     contact
(4) Delete all contacts
(0) Exit
'''

def create_user():
    name = input('Name: ')
    phone = input('Phone number: ')
    email = input('Email: ')
    return {'name': name, 'phone': phone, 'email': email}

contacts

choice = 1
while choice != 0:
    print(f'\n\n{menu}')
    choice = int(input('> '))
    if   choice == 0:
        print('Byee, have a great time')
        exit(0)
    elif choice == 1:
        user = create_user()
        for key, value in user.items():
            print(f'key: {key}\tvalue: {value}')
        # TODO: Add database interation
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        print('Invalid option')
