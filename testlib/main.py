from userlib import *



while True:
    print(f"registered users: {[user.username for user in user_list]}")
    print(f"logged users: {logged_users}")

    op = input('''================================================
Please choose an option: 
\n1 register \n2 login \n3 add contact \n4 remove contact \n5 print contact \n6 logout \n7 exit\n---\n''')

    if op == "1":
        print("---\nEnter registration data:")
        username = input("Username:\n")
        password = input("Password:\n")

        user = register_user(username, password)

    elif op == "2":
        username = input("Username:\n")
        password = input("Password:\n")

        login(username, password)

    elif op == "3":
        username = input("Add a contact for the user:\n")
        contact = input("Enter the contact:\n")

        add_new_contact(username, contact)

    elif op == "4":
        username = input("Remove a contact for the user:\n")
        contact = input("Enter the contact:\n")

        delete_contact(username, contact)

    elif op == "5":
        username = input("Print contacts of the user:\n")
        print_contact(username)

    elif op == "6":
        username = input("Log out the user:\n")

        logout(username)
    
    elif op == "7":
        print("---\nBye...")
        break

    else:
        print("---\nThere is no such option in the menu! Please try again...")

