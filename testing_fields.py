import unittest
from connect_to_database import DatabaseLifeChoices


class TestFields(unittest.TestCase):
    def test_field_type(self):
        username_field = DatabaseLifeChoices().select_usernames()
        id_field = DatabaseLifeChoices().select_user()
        surname_field = DatabaseLifeChoices().select_user()
        print(type(username_field[0][0]))
        print(type(id_field[0][0]))
        print(surname_field[0][2])
        self.assertEqual(type(id_field[0][0]), type(1))
        self.assertEqual(type(username_field[0][0]), type(""))
        self.assertEqual(type(surname_field[1][2]), type(""))


if __name__ == '__main__':
    unittest.main()
