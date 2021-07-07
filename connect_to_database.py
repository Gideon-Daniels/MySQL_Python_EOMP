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
        query_select_tables = "show tables"
        self.cursor.execute(query_select_tables)
        records = self.cursor.fetchall()
        return records

    def select_admin_table(self):
        query_select_table = "describe Admin"
        self.cursor.execute(query_select_table)
        records = self.cursor.fetchall()
        return records

    def select_user_table(self):
        query_select_table = "describe Admin"
        self.cursor.execute(query_select_table)
        records = self.cursor.fetchall()
        return records

    def select_User_In_Building_table(self):
        query_select_table = "describe User_In_Building"
        self.cursor.execute(query_select_table)
        records = self.cursor.fetchall()
        return records

    def select_Login_Details_table(self):
        query_select_table = "describe Login_Details"
        self.cursor.execute(query_select_table)
        records = self.cursor.fetchall()
        return records


print("Admin Table : ", DatabaseLifeChoices().select_admin_table())
print("User Table :", DatabaseLifeChoices().select_user_table())
print("User In Building :", DatabaseLifeChoices().select_User_In_Building_table())
print("Login Details :", DatabaseLifeChoices().select_Login_Details_table())
