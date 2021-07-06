class DatabaseLifeChoices:
    def __init__(self):
        # connecting to the database
        import mysql.connector as mysql
        self.db = mysql.connect(
            host="localhost",
            user="lifechoices",
            password="@Lifechoices1234",
            database="EOMP_Lifechoices_Database"
        )
        # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
        self.cursor = self.db.cursor()

    def select_all_tables(self):
        query_select_tables = "describe " \
                              "User_In_Building"
        self.cursor.execute(query_select_tables)
        records = self.cursor.fetchall()
        return records


all_tables = DatabaseLifeChoices().select_all_tables()
print(all_tables)
