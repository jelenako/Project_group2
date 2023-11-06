import multiprocessing
import time
import pythonhashmodule
class User:
    def __init__(self, username, password):

        if len(password) > 12:
            raise ValueError("Length greater than 12") 
        
        int(password)

        self.__username = username
        self.__password = password
        self.__list_of_contacts = []

    def __len__(self):
        return len(self.__list_of_contacts)
    
    def __str__(self):
        return f"Username: {self.__username} Password: {self.__password}" #kako ispis 
    
    
    def delete(self, username):
        for contact in self.__list_of_contacts :
            if(contact == username):
                self.__list_of_contacts.remove(contact)


    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self.__list_of_contacts):
            result = self.__list_of_contacts[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
        

    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username = username
        
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def list_of_contacts(self):
        return self.__list_of_contacts
    
    @list_of_contacts.setter
    def list_of_contacts(self, user):
        self.__list_of_contacts.append(user)
   
    @list_of_contacts.deleter
    def list_of_contacts(self):
        del self.__list_of_contacts[-1]
    
    
user_list = []
logged_users = []


def register_user(username, password):
    user = User(username, password)
    hashed_password = pythonhashmodule.hash_password(password)
    user.password = hashed_password
    if get_user(username) is None:
        user_list.append(user)
    else:
        print(f"Username: {username} already exists.")
    

def login(username, password):
    if not is_user_logged_in(username):
        user = get_user(username)
        if user is None:
            print("You need to register this user. Try to log in again.")
            return
    
        if (pythonhashmodule.check_password(user.password, password)):
            process = multiprocessing.Process(target=print_login_message(user))
            process.start()
            process.join()
            logged_users.append(user.username)
        else:
            print("Not valid password. Please log in again.")
    else:
        print(f"You {username} are already logged in")

    


def get_user(username):
    for user in user_list:
        if user.username == username:
            return user
    return None


def is_user_logged_in(username):
    for user in logged_users:
        if user == username:
            return True
    return False


def print_login_message(user):
    time.sleep(1)
    print(f"User {user.username} is logged in.")


def logout(username):
    if not is_user_logged_in(username):
        print(f"You {username} are not logged in")
        return 
    
    logged_users.remove(username)
    print(f"User with {username} log out")


def add_new_contact(username, contact):
    if is_user_logged_in(username):
        if get_user(contact) is not None:
            get_user(username).list_of_contacts = contact
        else:
            print(f"Contact {contact} not registered")
    else:
        print(f"You {username} not logged in.")


def delete_contact(username, contact):
    if is_user_logged_in(username):
        get_user(username).delete(contact)
    else:
        print(f"You {username} not logged in.")

def print_contact(username):
    if is_user_logged_in(username):
        user = get_user(username)
        iterator = iter(user)
        try:
            while True:
                print(next(iterator))
        except StopIteration:
            pass
    else:
        print(f"You {username} not logged in.")
            
               


# if __name__ == "__main__":
#    try:
#         user1 = User("dejan", "11111")
#         user2 = User("pero", "111211")
#         user3 = User("slavko", "11111")

#         register_user(user1.username, user1.password)
#         register_user(user2.username, user2.password)
#         register_user(user3.username, user3.password)

#         # for user in user_list:
#         #     print(user)

#         login(user1.username, user1.password)
#         add_new_contact(user1.username, user3.username)
#         add_new_contact(user1.username, user2.username)

#         delete_contact(user1.username, user2.username)

#         print_contact(user1.username,)

#         # print("eeeeeeeeeeeee")


#    except Exception as e:
#        print(e)