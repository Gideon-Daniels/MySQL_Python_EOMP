import unittest


class TestConnection(unittest.TestCase):
    def test_connection(self):
        host = "localhost"
        user = "lifechoices"
        password = "@Lifechoices1234"
        database = "EOMP_Lifechoices_Database"

        self.assertEqual(host, "localhost")
        self.assertEqual(user, "lifechoices")
        self.assertEqual(password, "@Lifechoices1234")
        self.assertEqual(database, "EOMP_Lifechoices_Database")

        import mysql.connector as mysql

        self.db = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="EOMP_Lifechoices_Database"
        )
        self.cursor = self.db.cursor()


if __name__ == '__main__':
    unittest.main()
