import multiprocessing
import time
class User:
    def __init__(self, username, password):

        if len(password) > 12:
            raise ValueError("Prekoracena duzina") 
        
        temp = int(password)

        self._username = username
        self._password = password
        self._list_of_contacts = []

    def __len__(self):
        return len(self._list_of_contacts)
    
    def __str__(self):
        return f"Username: {self._username} Password: {self._password}"
    
    def delete(self, username):
        for contact in self._list_of_contacts :
            if(contact.usernam == username):
                self._list_of_contacts.remove(contact)


    def __iter__(self):
        self.n = 0
        return self
    
    def __next__(self):
        if self.n < len(self._list_of_contacts):
            result = self._list_of_contacts[self.n]
            self.n += 1
            return result
        else:
            raise StopIteration
        

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        self._username = username
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password

    @property
    def list_of_contracts(self):
        return self._list_of_contacts
    
    @list_of_contracts.setter
    def list_of_contracts(self, user):
        self._list_of_contacts.append(user)
    
    
user_list = []

logged_users = []


def register_user(username, password):
    user = User(username, password)
    if get_user(username) is None:
        user_list.append(user)
    

def login(username, password):
   user = get_user(username)
   if user is None:
       print("You need to register this user")
       return
   
   if (user.password == password):
    #    print("Treba pokrenuti novi proces koji ne radi nista")
        process = multiprocessing.Process(target=print_login_message(user))
        process.start()
        process.join()
        logged_users.append(user)

def get_user(username):
    for user in user_list:
        if user.username == username:
            return user
    return None

def print_login_message(user):
    time.sleep(1)
    print(f"User {user.username} is logged in.")


def logout(username):
    for user in logged_users:
        if user.username == username:
            logged_users.remove(user)
            print("User logout")
            return
    print("You are not logged")




def add_new_contract(user, contract):
    for logged_user in logged_users:
        if user.username == logged_user.username :
            user.list_of_contracts = contract

def delete_contract(user, contract):
    for logged_user in logged_users:
        if user.username == logged_user.username :
            user.delete(contract.username)

def print_contract(user):
    for logged_user in logged_users:
        if user.username == logged_user.username :
            iterator = iter(user)
            try:
                while True:
                 item = next(iterator)
                 print(item)
            except StopIteration:
                pass
            
               


if __name__ == "__main__":
    print("Dobrodosao")
    user1 = User("dejan", "1111111")
    user2 = User("neko", "1111")
    user3 = User("pero", "222")
    # user1.password = "444"
    user1.list_of_contracts = user2
    user1.list_of_contracts = user3

    register_user("dejan", "1111111")
    login("dejan", "1111111")
    # time.sleep(2)
    logout("dejan")
    # print(len(user1))

    # iterator = iter(user1)

    # print(next(iterator))
    # print(next(iterator))
    