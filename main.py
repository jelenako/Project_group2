
import functions

if __name__ == "__main__":
    print("dobrodosao")

    while True :
        option = input("Choose function: \n r-register \n l-login \n a-add contact \n r-remove contact \n p-print contact \n lo-logout \n e-exit \n")

        if option == "r":
            print("========= Register function =========")
            username = input("Input username: ")
            password = input("Input password: ")
            functions.register_user(username, password)
            print("======================================")
        
        elif option == "l":
            print("========= Login funkcija ===========")
            username = input("Input username: ")
            password = input("Input password: ")
            functions.login(username, password)
            print("====================================")

        elif option == "a":
            print("========= Add contact ===========")
            username = input("Input your username: ")
            contact = input("Input contact username: ")
            functions.add_new_contact(username, contact)
            print("=================================")
        
        elif option == "r":
            print("======== Remove contact =========")
            username = input("Input your username: ")
            contact = input("Input contact username: ")
            functions.delete_contact(username, contact)
            print("=================================")

        
        elif option == "p":
            print("======== Print contact =========")
            username = input("Input your username: ")
            functions.print_contact(username)
            print("=================================")

        elif option == "lo":
            print("======== Logout function =======")
            username = input("Input your username: ")
            functions.logout(username)
            print("================================")
        
        else:
            print("Function does not exist")
        
