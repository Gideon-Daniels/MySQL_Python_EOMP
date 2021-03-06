from tkinter import messagebox


class DatabaseLifeChoices:
    def __init__(self):
        global mysql, errorcode
        try:
            # connecting to the database
            import mysql.connector as mysql
            from mysql.connector import errorcode
            self.db = mysql.connect(
                host="localhost",
                user="lifechoices",
                password="@Lifechoices1234",
                database="EOMP_Lifechoices_Database"
            )

            # creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
            self.cursor = self.db.cursor()

        except mysql.Error as error:
            if error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User authorization error")
            elif error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            else:
                print(error)

        #                                          DELETE STATEMENTS
    def delete_admin_data(self, admin_id):
        try:

            query_delete_data = "DELETE FROM Admin WHERE admin_id= %s "
            values = admin_id
            self.cursor.execute(query_delete_data, values)
            self.cursor.execute(query_delete_data)
            self.db.commit()
        except:
            messagebox.showerror("ERROR", "CONTACT DEV FOR MORE INFORMATION")

    def delete_user_data(self, user_id):
        try:
            user_id = user_id
            query_delete_data = "DELETE FROM Admin WHERE admin_id= %s "
            values = user_id
            self.cursor.execute(query_delete_data, values)
            self.cursor.execute(query_delete_data)
            self.db.commit()
        except:
            messagebox.showerror("ERROR", "CONTACT DEV FOR MORE INFORMATION")

        #                                           SELECT STATEMENTS
    def select_user(self):
        try:
            query_select_user = "SELECT * FROM User"
            self.cursor.execute(query_select_user)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")

    def select_admin_table(self):
        try:
            query_select_admin = "SELECT * FROM Admin"
            self.cursor.execute(query_select_admin)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")

    def select_log_in_details(self):
        try:
            query_select_log_in_details = "SELECT * FROM Log_in_details"
            self.cursor.execute(query_select_log_in_details)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")

    def select_attendance_register(self):
        try:
            query_select_attendance = "SELECT * FROM Attendance_register"
            self.cursor.execute(query_select_attendance)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")

    def select_next_of_kin(self):
        try:
            query_select_next_of_kin = "SELECT * FROM Next_of_kin"
            self.cursor.execute(query_select_next_of_kin)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")

    def select_usernames(self):
        try:
            query_select_next_of_kin = "SELECT username FROM User"
            self.cursor.execute(query_select_next_of_kin)
            records = self.cursor.fetchall()
            return records
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")
    #                                            UPDATE STATEMENTS

    def update_attendance_register(self, date_signed_in, signed_out):
        try:
            date_signed_in = date_signed_in
            signed_out = signed_out
            query_update = "UPDATE Attendance_register SET time_sign_out=%s WHERE date_signed_in=%s"
            values = (signed_out, date_signed_in)
            self.cursor.execute(query_update, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "CONTACT DEV FOR MORE INFORMATION")
        #                                            INSERT STATEMENTS

# 7
    def insert_user(self, name, surname, cell_num, kin_num, admin_rights, password, user_id_num,
                    ):
        try:
            name = str(name)
            surname = str(surname)
            cell_num = int(cell_num)
            kin_num = int(kin_num)
            admin_rights = bool(admin_rights)
            password = str(password)
            user_id_num = str(user_id_num)
            query_insert = "INSERT INTO Next_of_kin VALUES (%s,%s,%s,%s,%s,%s,%s)"
            values = (name, surname, cell_num, kin_num, admin_rights, password, user_id_num)
            self.cursor.execute(query_insert, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "SYSTEM ERROR , CONTACT ADMIN")

# 8
    def insert_admin(self, name, cell_num, kin_num, admin_rights, password, user_id_num, ):
        try:
            name = name
            cell_num = cell_num
            kin_num = kin_num
            admin_rights = admin_rights
            password = password
            user_id_num = user_id_num
            query_insert = "INSERT INTO Next_of_kin VALUES (%s,%s,%s,%s,%s,%s)"
            values = (name, cell_num, kin_num, admin_rights, password, user_id_num)
            self.cursor.execute(query_insert, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "SYSTEM ERROR, CONTACT ADMIN")

# 5
    def insert_attendance_register(self, userid, name, date_signed_in, time_signed_in, time_signed_out):
        try:
            userid = userid
            name = name
            date_signed_in = date_signed_in
            time_signed_in = time_signed_in
            time_signed_out = time_signed_out
            query_insert = "INSERT INTO Attendance_register VALUES (%s,%s,%s,%s,%s)"
            values = (userid, name, date_signed_in, time_signed_in, time_signed_out)
            self.cursor.execute(query_insert, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "INFORMATION ENTERED IS INCORRECT , CONTACT ADMIN")

# 3
    def insert_log_in_details(self, userid, name, password):
        try:
            userid = userid
            name = name
            password = password
            query_insert = "INSERT INTO Next_of_kin VALUES (%s,%s,%s)"
            values = (userid, name, password)
            self.cursor.execute(query_insert, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "INFORMATION ENTERED IS INCORRECT , CONTACT ADMIN")

# 3
    def insert_next_of_kin(self, userid, name, cell_num):
        try:
            userid = userid
            name = name
            cell_num = cell_num
            query_insert = "INSERT INTO Next_of_kin VALUES (%s,%s,%s)"
            values = (userid, name, cell_num)
            self.cursor.execute(query_insert, values)
            self.db.commit()
        except:
            messagebox.showwarning("WARNING", "INFORMATION ENTERED IS INCORRECT , CONTACT ADMIN")


# PRINTING ALL TABLE INFORMATION TO THE TERMINAL
print("Admin Table : ", DatabaseLifeChoices().select_admin_table())
print("User : ", DatabaseLifeChoices().select_user())
print("Attendance Register : ", DatabaseLifeChoices().select_attendance_register())
print("Login Details : ", DatabaseLifeChoices().select_log_in_details())
print("Next Of Kin : ", DatabaseLifeChoices().select_next_of_kin())
