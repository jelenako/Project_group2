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
        user = User("user1", "password1")
        self.user_list.append(user)
        self.assertEqual(user.username, "user1")
        self.assertEqual(user.password, "password1")
        self.assertTrue(user in self.user_list)

    def test_create_user_invalid_password(self):
        # Test creating a user with an invalid password
        with self.assertRaises(ValueError):
            User("user2", "password1234567890")

    def test_set_get_username(self):
        # Test getter and setter for username
        user = User("user3", "password3")
        user.username = "new_username"
        self.assertEqual(user.username, "new_username")

    def test_set_get_password(self):
        # Test getter and setter for password
        user = User("user4", "password4")
        user.password = "new_password"
        self.assertEqual(user.password, "new_password")

    def test_set_get_delete_contact(self):
        # Test getter, setter, and deleter for contact
        user = User("user5", "password5")
        user.list_of_contacts = "contact1"
        user.list_of_contacts = "contact2"
        self.assertIn("contact1", user.list_of_contacts)
        self.assertIn("contact2", user.list_of_contacts)

        del user.list_of_contacts
        self.assertEqual(user.list_of_contacts, [])

    def test_length_method(self):
        # Test the __len__ method
        user = User("user1", "password1")
        self.assertEqual(len(user), 0)
        user.list_of_contacts = "contact1"
        user.list_of_contacts = "contact2"
        self.assertEqual(len(user), 2)

    def test_str_method(self):
        # Test the __str__ method
        user = User("user2", "password2")
        self.assertEqual(str(user), "Username: user2 Password: password2")

    def test_iterator(self):
        # Test the __iter__ and __next__ methods
        user = User("user3", "password3")
        user.list_of_contacts = "contact1"
        user.list_of_contacts = "contact2"
        iterator = iter(user)
        self.assertEqual(next(iterator), "contact1")
        self.assertEqual(next(iterator), "contact2")
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_register_with_valid_params(self):
        # Test registering a user with valid parameters
        register_user("user4", "password4")
        user = get_user("user4")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "user4")

    def test_register_with_invalid_params(self):
        # Test registering a user with invalid parameters
        with self.assertRaises(ValueError):
            register_user("user5", "password1234567890")

    def test_login_with_valid_params(self):
        # Test logging in with valid parameters
        register_user("user6", "password6")
        login("user6", "password6")
        self.assertIn("user6", self.logged_users)

    def test_login_with_invalid_params(self):
        # Test logging in with invalid parameters
        register_user("user7", "password7")
        with self.assertRaises(ValueError):
            login("user7", "invalid_password")

    def test_login_with_non_existing_user(self):
        # Test logging in with a non-existing user
        with self.assertRaises(ValueError):
            login("non_existing_user", "password")

    def test_logout(self):
        # Test logging out
        register_user("user8", "password8")
        login("user8", "password8")
        logout("user8")
        self.assertNotIn("user8", self.logged_users)

    def test_logout_user_not_logged_in(self):
        # Test logging out a user that is not logged in
        with self.assertRaises(ValueError):
            logout("user9")

    def test_add_contact_valid(self):
        # Test adding a contact with a valid user
        register_user("user10", "password10")
        login("user10", "password10")
        add_new_contact("user10", "contact1")
        user = get_user("user10")
        self.assertIn("contact1", user.list_of_contacts)

    def test_add_contact_user_not_logged_in(self):
        # Test adding a contact with a user that is not logged in
        register_user("user11", "password11")
        with self.assertRaises(ValueError):
            add_new_contact("user11", "contact2")

    def test_remove_contact_valid(self):
        # Test removing a contact with a valid user
        register_user("user12", "password12")
        login("user12", "password12")
        add_new_contact("user12", "contact3")
        delete_contact("user12", "contact3")
        user = get_user("user12")
        self.assertNotIn("contact3", user.list_of_contacts)

    def test_remove_contact_user_not_logged_in(self):
        # Test removing a contact with a user that is not logged in
        register_user("user13", "password13")
        with self.assertRaises(ValueError):
            delete_contact("user13", "contact4")

    def test_print_contact(self):
        # Test printing contacts with a logged-in user
        register_user("user14", "password14")
        login("user14", "password14")
        add_new_contact("user14", "contact5")
        add_new_contact("user14", "contact6")
        user = get_user("user14")
        contacts = []
        for contact in user:
            contacts.append(contact)
        self.assertEqual(contacts, ["contact5", "contact6"])

    def test_print_contact_user_not_logged_in(self):
        # Test printing contacts with a user that is not logged in
        register_user("user15", "password15")
        user = get_user("user15")
        contacts = []
        for contact in user:
            contacts.append(contact)
        self.assertEqual(contacts, [])

    # mocked

    @patch('functions.pythonhashmodule.hash_password')
    def test_register_with_valid_params(self, mock_hash_password):
        # Test registering a user with valid parameters
        username = "user4"
        password = "password4"

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
        user = User("user5", "password5")

        # Mock the delete method of the User class
        user.delete = Mock()

        # Perform an action that calls the mocked method
        user.delete("contact1")

        # Assert that the mocked method was called with the expected arguments
        user.delete.assert_called_once_with("contact1")


    @patch('functions.User.__next__')
    def test_mock_iterator(self, mock_next):
        # Test mocking the __next__ method of the User class (iterator)
        user = User("user6", "password6")

        # Configure the behavior of the mock
        mock_next.side_effect = ["contact1", "contact2", StopIteration]

        # Iterate over the user to call the mocked __next__ method
        contacts = []
        for contact in user:
            contacts.append(contact)

        # Assert that the mocked __next__ method was called as expected
        mock_next.assert_has_calls([Mock(contact) for contact in ["contact1", "contact2"]])

        # Ensure that the iteration stops correctly
        self.assertEqual(contacts, ["contact1", "contact2"])


