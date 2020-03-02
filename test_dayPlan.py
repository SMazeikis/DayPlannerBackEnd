import unittest
from dayPlan import makeDay, restaurant_info


class testUser(unittest.TestCase):

    def setUp(self):
        self.userId = "AtkMr1OLlCaTv42JdnBfTEojPeF3"

    def test_restaurantInfo(self):
        print("testing return type of restaurant_info")
        self.assertEqual(list, type(restaurant_info("indian")))

    def test_dayPlan(self):
        print("testing return type of makeDay")
        self.assertEqual(dict, type(makeDay(self.userId)))


if __name__ == "__main__":
    unittest.main()
