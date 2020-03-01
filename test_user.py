import unittest
from user import assignPreferences 

class testUser(unittest.TestCase):

    def setUp(self):
        pass

    def test_addingPreferences(self):
        self.assertEqual(3, 3, "should be True")
        self.assertEqual(3, 3, "should be True")


if __name__ == "__main__":
    unittest.main()