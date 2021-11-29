import unittest
from Database import *

class TestDatabase(unittest.TestCase):

    def test_connectToServer(self):
        self.assertTrue(Database.connectToServer(), "Must return true.\n")
        self.assertFalse(Database.connectToServer(), "Must return false.\n")

    def test_getUser(self):
        self.assertFalse(Database.getUser("1234"), "Must return false.\n")
        self.assertTrue(Database.getUser("123"), "Must return true.\n")

    def test_register(self):
        self.assertTrue(Database.register(), "Must return true")


if __name__ == '__main__':
    unittest.main()