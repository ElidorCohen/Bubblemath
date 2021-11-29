import unittest
from Database import *

class TestDatabase(unittest.TestCase):

    def test_connectToServer(self):
        self.assertTrue(Database.is_connected(True), "Must return true.\n")
        self.assertFalse(Database.is_connected(False), "Must return false.\n")


if __name__ == '__main__':
    unittest.main()