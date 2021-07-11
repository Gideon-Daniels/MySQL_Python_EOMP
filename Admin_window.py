from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from connect_to_database import DatabaseLifeChoices


class AdminWindow:

    def __init__(self):
        # creating window
        self.window = Tk()
        self.window.title("Login Page")
        self.window.geometry("1550x720")
        self.window.config(bg="#323232")

        # creating widgets
        # Frames
        self.frame_header = Frame(self.window, width=100, height=100, bg="#78cc6d")
        self.frame_header.pack(fill="both")

        self.frame_buttons = Frame(self.window, width=100, height=240, bg="#323232")
        self.frame_buttons.place(x=50, y=125)

        self.frame_user = Frame(self.window, width=1050, height=425, bg="#323232")

        self.frame_admin = Frame(self.window, width=1050, height=425, bg="#323232")

        self.frame_attendance = Frame(self.window, width=1050, height=425, bg="#323232")

        self.frame_footer = Frame(self.window, width=100, height=100, bg="#78cc6d")
        self.frame_footer.pack(fill="both", side="bottom")

        # Tree View
        self.tree_view_admin = ttk.Treeview(self.frame_admin)
        self.tree_view_attendance = ttk.Treeview(self.frame_attendance)
        self.tree_view_users = ttk.Treeview(self.frame_user)

        # Labels
        #                                 LABEL FOR HEADER FRAME
        self.label_header_one = Label(self.frame_header, text="LIFE CHOICES")
        self.label_header_one.place(y=30, x=600)
        self.label_header_one.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")
        self.label_header_two = Label(self.frame_header, text="ADMINISTRATION")
        self.label_header_two.place(y=30, x=800)
        self.label_header_two.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")

        # Buttons
        self.button_attendance = Button(self.frame_buttons, text="ATTENDANCE REGISTER",
                                        command=self.attendance_register)
        self.button_attendance.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_attendance.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_attendance.pack(padx=20, pady=10)
        # self.button_attendance.config(state=DISABLED)

        self.button_admin = Button(self.frame_buttons, text="ADMIN", command=self.admin)
        self.button_admin.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_admin.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_admin.pack(padx=20, pady=10)
        # self.button_admin.config(state=DISABLED)

        self.button_users = Button(self.frame_buttons, text="USERS", command=self.users)
        self.button_users.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_users.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_users.pack(padx=20, pady=10)
        # self.button_users.config(state=DISABLED)

        self.button_next_of_kin = Button(self.frame_buttons, text="NEXT OF KIN", )
        self.button_next_of_kin.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_next_of_kin.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_next_of_kin.pack(padx=20, pady=10)
        self.button_next_of_kin.config(state=DISABLED)

        self.button_add = Button(self.frame_buttons, text="ADD", )
        self.button_add.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_add.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_add.pack(padx=20, pady=10)
        self.button_add.config(state=DISABLED)

        self.button_edit = Button(self.frame_buttons, text="EDIT", )
        self.button_edit.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_edit.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_edit.pack(padx=20, pady=10)
        self.button_edit.config(state=DISABLED)

        self.button_delete = Button(self.frame_buttons, text="DELETE", command=self.delete_data)
        self.button_delete.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_delete.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_delete.pack(padx=20, pady=10)

        self.button_exit = Button(self.frame_buttons, text="EXIT", command=self.exit_window)
        self.button_exit.config(width=20, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_exit.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_exit.pack(padx=20, pady=10)

        # repeatedly show window on screen
        self.window.mainloop()

    #                                                    END OF CONSTRUCTOR

    # functions to delete data from tables
    def exit_window(self):
        self.window.destroy()

    def delete_data(self):
        self.selected = self.tree_view_admin.selection()
        for row_id in self.selected:
            selected_id = int(row_id) + 1
            DatabaseLifeChoices().delete_admin_data(selected_id)
            self.tree_view_admin.delete(row_id)

    #   functions to select and display tables
    def attendance_register(self):
        self.frame_attendance.place(x=400, y=125)
        data_attendance = DatabaseLifeChoices().select_attendance_register()
        count = 0
        # define our columns
        self.tree_view_attendance["columns"] = ("User ID", "Name", "Date Signed In", "Time Signed In", "Time Signed "
                                                                                                       "Out")
        # Format Our Columns
        self.tree_view_attendance.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_attendance.column("User ID", anchor=W, width=150)
        self.tree_view_attendance.column("Name", anchor=W, width=100)
        self.tree_view_attendance.column("Date Signed In", anchor=W, width=150)
        self.tree_view_attendance.column("Time Signed In", anchor=W, width=150)
        self.tree_view_attendance.column("Time Signed Out", anchor=W, width=150)

        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.tree_view_attendance.heading("User ID", text="User ID", anchor=CENTER)
        self.tree_view_attendance.heading("Name", text="Name", anchor=CENTER)
        self.tree_view_attendance.heading("Date Signed In", text="Date Signed In", anchor=CENTER)
        self.tree_view_attendance.heading("Time Signed In", text="Date Signed In", anchor=CENTER)
        self.tree_view_attendance.heading("Time Signed Out", text="Date Signed Out", anchor=CENTER)

        self.tree_view_attendance.pack(padx=100, pady=100)

        # Algorithm adding data to table

        for record in data_attendance:
            self.tree_view_attendance.insert(parent="", index="end", iid=count, text="", values=(
                record[0],
                record[1],
                record[2],
                record[3],
                record[4]
            )
                                             )
            count += 1
        # self.frame_admin.destroy()
        self.button_attendance.config(state=DISABLED)

    def admin(self):
        self.frame_admin.place(x=380, y=180)
        data_admin = DatabaseLifeChoices().select_admin_table()
        count = 0
        # define our columns
        self.tree_view_admin["columns"] = ("Admin ID", "Name", "Surname", "Cell Number",
                                           "Kin Number", "Admin Rights", "Password", "Date Signed In")
        # Format Our Columns
        self.tree_view_admin.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_admin.column("Admin ID", anchor=W, width=150)
        self.tree_view_admin.column("Name", anchor=W, width=100)
        self.tree_view_admin.column("Surname", anchor=W, width=100)
        self.tree_view_admin.column("Cell Number", anchor=W, width=150)  # phantom column
        self.tree_view_admin.column("Kin Number", anchor=W, width=150)
        self.tree_view_admin.column("Admin Rights", anchor=W, width=150)
        self.tree_view_admin.column("Password", anchor=W, width=150)
        self.tree_view_admin.column("Date Signed In", anchor=W, width=150)
        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.tree_view_admin.heading("Admin ID", text="Admin ID", anchor=CENTER)
        self.tree_view_admin.heading("Name", text="Name", anchor=CENTER)
        self.tree_view_admin.heading("Surname", text="Surname", anchor=CENTER)
        self.tree_view_admin.heading("Cell Number", text="Cell Number", anchor=CENTER)
        self.tree_view_admin.heading("Kin Number", text="Kin Number", anchor=CENTER)
        self.tree_view_admin.heading("Admin Rights", text="Admin Rights", anchor=CENTER)
        self.tree_view_admin.heading("Password", text="Password", anchor=CENTER)
        self.tree_view_admin.heading("Date Signed In", text="Date Signed In", anchor=CENTER)
        self.tree_view_admin.pack(padx=10, pady=10)

        # Algorithm adding data to table

        for record in data_admin:
            admin_rights = "NO"
            if record[0] == 1:
                admin_rights = "YES"
            self.tree_view_admin.insert(parent="", index="end", iid=count, text="", values=(
                record[0],
                record[1],
                record[2],
                record[3],
                record[4],
                admin_rights,
                record[6],
                record[7],
            )
                                        )
            count += 1
        # self.button_attendance.config(state=NORMAL)

    def users(self):
        self.frame_user.place(x=280, y=180)
        data_user = DatabaseLifeChoices().select_user()
        count = 0
        # define our columns
        self.tree_view_users["columns"] = ("User ID", "Name", "Surname", "Cell Number",
                                           "Kin Number", "Admin Rights", "Password", "ID Number", "Date Signed In")
        # Format Our Columns
        self.tree_view_users.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_users.column("User ID", anchor=W, width=150)
        self.tree_view_users.column("Name", anchor=W, width=100)
        self.tree_view_users.column("Surname", anchor=W, width=100)
        self.tree_view_users.column("Cell Number", anchor=W, width=150)  # phantom column
        self.tree_view_users.column("Kin Number", anchor=W, width=150)
        self.tree_view_users.column("Admin Rights", anchor=W, width=150)
        self.tree_view_users.column("Password", anchor=W, width=150)
        self.tree_view_users.column("ID Number", anchor=W, width=150)
        self.tree_view_users.column("Date Signed In", anchor=W, width=150)
        # Create Headings
        # self.tree_view_users.heading("#0", text="", anchor=CENTER)
        self.tree_view_users.heading("User ID", text="User ID", anchor=CENTER)
        self.tree_view_users.heading("Name", text="Name", anchor=CENTER)
        self.tree_view_users.heading("Surname", text="Surname", anchor=CENTER)
        self.tree_view_users.heading("Cell Number", text="Cell Number", anchor=CENTER)
        self.tree_view_users.heading("Kin Number", text="Kin Number", anchor=CENTER)
        self.tree_view_users.heading("Admin Rights", text="Admin Rights", anchor=CENTER)
        self.tree_view_users.heading("Password", text="Password", anchor=CENTER)
        self.tree_view_users.heading("ID Number", text="ID Number", anchor=CENTER)
        self.tree_view_users.heading("Date Signed In", text="Signed In", anchor=CENTER)
        self.tree_view_users.pack(padx=10, pady=10)

        # Algorithm adding data to table

        for record in data_user:
            admin_rights = "NO"
            if record[5] == 1:
                admin_rights = "YES"
            self.tree_view_users.insert(parent="", index="end", iid=count, text="", values=(
                record[0],
                record[1],
                record[2],
                record[3],
                record[4],
                admin_rights,
                record[6],
                record[7],
            )
                                        )
            count += 1
        # self.button_attendance.config(state=NORMAL)
        # self.button_users.config(state=DISABLED)


AdminWindow()
