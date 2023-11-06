import unittest
from userlib.functions import *
from unittest.mock import patch, Mock

class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.user_list = []
        self.logged_users = []

    def tearDown(self):
        self.user_list.clear()
        self.logged_users.clear()

    def test_create_user_valid_username_password(self):
        # Test creating a user with a valid username and password
        user = User("user1", "11111")
        self.user_list.append(user)
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "11111")
        self.assertTrue(user in self.user_list)

    def test_create_user_invalid_password(self):
        # Test creating a user with an invalid password
        with self.assertRaises(ValueError):
            User("user2", "password1234567890")

    def test_set_get_username(self):
        # Test getter and setter for username
        user = User("user3", "33333")
        user.username = "new_username"
        self.assertEqual(user.username, "new_username")

    def test_set_get_password(self):
        # Test getter and setter for password
        user = User("user4", "44444")
        user.password = "new_password"
        self.assertEqual(user.password, "new_password")

    def test_set_get_delete_contact(self):
        # Test getter, setter, and deleter for contact
        user = User("user5", "55555")
        user.list_of_contacts = "contact1"
        self.assertIn("contact1", user.list_of_contacts)

        del user.list_of_contacts
        self.assertEqual(user.list_of_contacts, [])

    def test_length_method(self):
        # Test the __len__ method
        user = User("user1", "11111")
        self.assertEqual(len(user), 0)
        user.list_of_contacts = "contact1"
        user.list_of_contacts = "contact2"
        self.assertEqual(len(user), 2)

    def test_str_method(self):
        # Test the __str__ method
        user = User("user2", "22222")
        self.assertEqual(str(user), "Username: user2 Password: 22222")

    def test_iterator(self):
        # Test the __iter__ and __next__ methods
        user = User("user3", "33333")
        user.list_of_contacts = "contact1"
        user.list_of_contacts = "contact2"
        iterator = iter(user)
        self.assertEqual(next(iterator), "contact1")
        self.assertEqual(next(iterator), "contact2")
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_register_with_valid_params(self):
        # Test registering a user with valid parameters
        register_user("user4", "44444")
        user = get_user("user4")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "user4")

    def test_register_with_invalid_params(self):
        # Test registering a user with invalid parameters
        with self.assertRaises(ValueError):
            register_user("user5", "password1234567890")

    def test_login_with_valid_params(self):
        # Test logging in with valid parameters
        register_user("user6", "66666")
        login("user6", "66666")
        self.assertEqual(True, is_user_logged_in("user6"))

    def test_login_with_invalid_params(self):
        # Test logging in with invalid parameters
        register_user("user7", "77777")
        login("user7", "invalid_password")
        self.assertNotIn("user11", self.logged_users)

    def test_login_with_non_existing_user(self):
        # Test logging in with a non-existing user
        login("non_existing_user", "password")
        self.assertNotIn("non_existing_user", self.logged_users)
        

    def test_logout(self):
        # Test logging out
        register_user("user8", "88888")
        login("user8", "88888")
        logout("user8")
        self.assertNotIn("user8", self.logged_users)

    def test_logout_user_not_logged_in(self):
        # Test logging out a user that is not logged in
        logout("user9")
        self.assertNotIn("user9", self.logged_users)

    def test_add_contact_valid(self):
        # Test adding a contact with a valid user
        register_user("user10", "101010")
        register_user("user11", "111111")
        login("user10", "101010")
        add_new_contact("user10", "user11")
        user = get_user("user10")
        print(user.list_of_contacts)
        self.assertIn("user11", user.list_of_contacts)

    def test_add_contact_user_not_logged_in(self):
        # Test adding a contact with a user that is not logged in
        register_user("user11", "111111")
        register_user("user22", "222222")
        add_new_contact("user11", "user22")
        user = get_user("user11")
        self.assertNotIn("user22", user.list_of_contacts)

    def test_remove_contact_valid(self):
        # Test removing a contact with a valid user
        register_user("user12", "121212")
        register_user("user15", "151515")
        login("user12", "121212")
        add_new_contact("user12", "user15")
        delete_contact("user12", "user15")
        user = get_user("user12")
        self.assertNotIn("user15", user.list_of_contacts)

    def test_remove_contact_user_not_logged_in(self):
        # Test removing a contact with a user that is not logged in
        register_user("user13", "13131313")
        register_user("user33", "33333333")
        login("user13", "13131313")
        add_new_contact("user13", "user33")
        logout("user13")
        delete_contact("user13", "user333")
        user = get_user("user13")
        self.assertIn("user33", user.list_of_contacts)

    def test_print_contact(self):
        # Test printing contacts with a logged-in user
        register_user("user14", "141414")
        register_user("user55", "5555555")
        register_user("user66", "6666666")
        login("user14", "141414")
        add_new_contact("user14", "user55")
        add_new_contact("user14", "user66")
        user = get_user("user14")
        contacts = []
        for contact in user.list_of_contacts:
            contacts.append(contact)
        self.assertEqual(contacts, ["user55", "user66"])

    def test_print_contact_user_not_logged_in(self):
        # Test printing contacts with a user that is not logged in
        register_user("user75", "151515")
        user = get_user("user75")
        contacts = []
        for contact in user:
            contacts.append(contact)
        self.assertEqual(contacts, [])

    # mocked

    @patch('functions.pythonhashmodule.hash_password')
    def test_register_with_valid_params(self, mock_hash_password):
        # Test registering a user with valid parameters
        username = "user4"
        password = "44444"

        # Configure the behavior of the mock
        mock_hash_password.return_value = "hashed_password"

        register_user(username, password)
        user = get_user(username)
        self.assertIsNotNone(user)
        self.assertEqual(user.username, username)

        # Ensure that the mocked function was called with the expected arguments
        mock_hash_password.assert_called_once_with(password)

    def test_mock_user_method(self):
        # Test mocking a method within the User class
        user = User("user5", "55555")

        # Mock the delete method of the User class
        user.delete = Mock()

        # Perform an action that calls the mocked method
        user.delete("contact1")

        # Assert that the mocked method was called with the expected arguments
        user.delete.assert_called_once_with("contact1")


    @patch('functions.User.__next__')
    def test_mock_iterator(self, mock_next):
        # Test mocking the __next__ method of the User class (iterator)
        user = User("user6", "666666")

        # Configure the behavior of the mock
        mock_next.side_effect = ["contact1", "contact2", StopIteration]

        # Iterate over the user to call the mocked __next__ method
        contacts = []
        for contact in user:
            contacts.append(contact)

        # Assert that the mocked __next__ method was called as expected
        mock_next.assert_has_calls([Mock(contact) for contact in ["contact1", "contact2"]])

        # Ensure that the iteration stops correctly
        print("============================================================")
        print(contacts)
        self.assertEqual(contacts, ["contact1", "contact2"])



if __name__ == "__main__":
    unittest.main()


