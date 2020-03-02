import unittest
from user import assignPreferences


class testUser(unittest.TestCase):

    def setUp(self):
        someList = [
            {
                "html": 'AMERICAN',
                "id": 0,
                "clicked": True,
                "style": {
                    'background-image': 'url(' + "require('../assets/americanfood.jpg')" + ')',
                    'background-size': 'cover',
                }
            },
            {
                "html": 'INDIAN',
                "id": 1,
                "clicked": False,
                "style": {
                    'background-image': 'url(' + "require('../assets/indianfood.jpg')" + ')',
                    'background-size': 'cover',
                }
            },
            {
                "html": 'ITALIAN',
                "id": 2,
                "clicked": False,
                "style": {
                    'background-image': 'url(' + "require('../assets/italianfood4.jpg')" + ')',
                    'background-size': 'cover',
                }
            },
            {
                "html": 'JAPANESE',
                "id": 3,
                "clicked": False,
                "style": {
                    'background-image': 'url(' + "require('../assets/japanesefood5.jpg')" + ')',
                    'background-size': 'cover',
                }
            }
        ]
        someList1 = [
            {
                "html": 'TOURISM',
                "id": 0,
                "clicked": True,
                "style": {
                    'background-image': 'url(' + "require('../assets/tourism.jpg')" + ')',
                    'background-size': 'cover',
                }
            },
            {
                "html": 'indoors',
                "id": 1,
                "clicked": False,
                "style": {
                    'background': '#4bbfc3'
                }
            },
            {
                "html": 'slide3',
                "id": 2,
                "clicked": False,
                "style": {
                    'background': '#7baabe'
                }
            },
            {
                "html": 'slide4',
                "id": 3,
                "clicked": False,
                "style": {
                    'background': '#7baabe'
                }
            }
        ]
        self.preferenceData = {"userId": "AtkMr1OLlCaTv42JdnBfTEojPeF3",
                               "foodPreferences": someList,
                               "activityPreferences": someList1}

    def test_addingPreferences(self):
        print("testing Preference assignment response")
        self.assertEqual(assignPreferences(self.preferenceData), "ok")


if __name__ == "__main__":
    unittest.main()
