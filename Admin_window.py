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
        self.frame_details = Frame(self.window, width=1440, height=440, bg="#78cc6d")
        self.frame_details.place(x=60, y=120)
        self.frame_buttons = Frame(self.window, width=100, height=240, bg="#323232")
        self.frame_buttons.place(x=120, y=125)
        self.frame_footer = Frame(self.window, width=100, height=100, bg="#78cc6d")
        self.frame_footer.pack(fill="both", side="bottom")

        # Labels
        #                                 LABEL FOR HEADER FRAME
        self.label_header_one = Label(self.frame_header, text="LIFE CHOICES")
        self.label_header_one.place(y=30, x=600)
        self.label_header_one.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")
        self.label_header_two = Label(self.frame_header, text="ADMINISTRATION")
        self.label_header_two.place(y=30, x=800)
        self.label_header_two.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")

        # Tree View
        self.tree_view_admin = ttk.Treeview(self.window)
        self.tree_view_attendance = ttk.Treeview(self.window)
        self.tree_view_users = ttk.Treeview(self.window)
        # Buttons
        self.button_attendance = Button(self.frame_buttons, text="ATTENDANCE REGISTER",
                                        command=self.attendance_register)
        self.button_attendance.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_attendance.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_attendance.pack(padx=20, pady=10)
        self.button_attendance.config(state=DISABLED)

        self.button_admin = Button(self.frame_buttons, text="ADMIN", command=self.admin)
        self.button_admin.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_admin.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_admin.pack(padx=20, pady=10)

        self.button_users = Button(self.frame_buttons, text="USERS", command=self.users)
        self.button_users.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_users.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_users.pack(padx=20, pady=10)
        self.button_users.config(state=DISABLED)

        self.button_next_of_kin = Button(self.frame_buttons, text="NEXT OF KIN", )
        self.button_next_of_kin.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_next_of_kin.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_next_of_kin.pack(padx=20, pady=10)
        self.button_next_of_kin.config(state=DISABLED)

        self.button_login_details = Button(self.frame_buttons, text="LOGIN DETAILS", )
        self.button_login_details.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_login_details.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_login_details.pack(padx=20, pady=10)
        self.button_login_details.config(state=DISABLED)

        self.button_edit = Button(self.frame_buttons, text="EDIT", )
        self.button_edit.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_edit.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_edit.pack(padx=20, pady=10)
        self.button_edit.config(state=DISABLED)

        self.button_delete = Button(self.frame_buttons, text="DELETE", command=self.delete_data)
        self.button_delete.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_delete.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_delete.pack(padx=20, pady=10)

        self.button_delete = Button(self.frame_buttons, text="EXIT", command=self.exit_window)
        self.button_delete.config(width=20, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_delete.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_delete.pack(padx=20, pady=10)

        # repeatedly show window on screen
        self.window.mainloop()

    #                                                    END OF CONSTRUCTOR

    # functions to delete data from tables
    def exit_window(self):
        self.window.destroy()

    def delete_data(self):
        self.selected = self.tree_view_admin.selection()
        for row_id in self.selected:
            selected_id = int(row_id)+1
            DatabaseLifeChoices().delete_admin_data(selected_id)
            self.tree_view_admin.delete(row_id)

    #   functions to select and display tables
    def attendance_register(self):
        self.data_user = DatabaseLifeChoices().select_user()
        self.count = 0
        # define our columns
        self.tree_view_attendance["columns"] = ("Admin ID", "Name", "Surname", "Cell Number",
                                                "Kin Number", "Admin Rights", "Password", "Date Signed In")
        # Format Our Columns
        self.tree_view_attendance.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_attendance.column("Admin ID", anchor=W, width=150)
        self.tree_view_attendance.column("Name", anchor=W, width=100)
        self.tree_view_attendance.column("Surname", anchor=W, width=100)
        self.tree_view_attendance.column("Cell Number", anchor=W, width=150)  # phantom column
        self.tree_view_attendance.column("Kin Number", anchor=W, width=150)
        self.tree_view_attendance.column("Admin Rights", anchor=W, width=150)
        self.tree_view_attendance.column("Password", anchor=W, width=150)
        self.tree_view_attendance.column("Date Signed In", anchor=W, width=150)
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
        self.tree_view_admin.place(x=380, y=190)

        # Algorithm adding data to table

        for record in self.data_user:
            admin_rights = "NO"
            if record[0] == 1:
                admin_rights = "YES"
            self.tree_view_admin.insert(parent="", index="end", iid=self.count, text="", values=(
                admin_rights,
                record[1],
                record[2],
                record[3],
                record[4],
                admin_rights,
                record[6],
                record[7],
            )
                                        )
            self.count += 1

    def admin(self):
        self.data_admin = DatabaseLifeChoices().select_user()
        self.count = 0
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
        self.tree_view_admin.place(x=380, y=190)

        # Algorithm adding data to table

        for record in self.data_admin:
            admin_rights = "NO"
            if record[0] == 1:
                admin_rights = "YES"
            self.tree_view_admin.insert(parent="", index="end", iid=self.count, text="", values=(
                admin_rights,
                record[1],
                record[2],
                record[3],
                record[4],
                admin_rights,
                record[6],
                record[7],
            )
                                        )
            self.count += 1

    def users(self):
        self.data_user = DatabaseLifeChoices().select_user()
        self.count = 0
        # define our columns
        self.tree_view_attendance["columns"] = ("Admin ID", "Name", "Surname", "Cell Number",
                                                "Kin Number", "Admin Rights", "Password", "Date Signed In")
        # Format Our Columns
        self.tree_view_attendance.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_attendance.column("Admin ID", anchor=W, width=150)
        self.tree_view_attendance.column("Name", anchor=W, width=100)
        self.tree_view_attendance.column("Surname", anchor=W, width=100)
        self.tree_view_attendance.column("Cell Number", anchor=W, width=150)  # phantom column
        self.tree_view_attendance.column("Kin Number", anchor=W, width=150)
        self.tree_view_attendance.column("Admin Rights", anchor=W, width=150)
        self.tree_view_attendance.column("Password", anchor=W, width=150)
        self.tree_view_attendance.column("Date Signed In", anchor=W, width=150)
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
        self.tree_view_admin.place(x=380, y=190)

        # Algorithm adding data to table

        for record in self.data_user:
            admin_rights = "NO"
            if record[0] == 1:
                admin_rights = "YES"
            self.tree_view_admin.insert(parent="", index="end", iid=self.count, text="", values=(
                admin_rights,
                record[1],
                record[2],
                record[3],
                record[4],
                admin_rights,
                record[6],
                record[7],
            )
                                        )
            self.count += 1


AdminWindow()
