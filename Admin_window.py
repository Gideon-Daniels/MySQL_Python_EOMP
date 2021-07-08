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
        # define our columns
        self.tree_view_admin["columns"] = ("Admin_rights", "Name", "Surname", "Phone Number", "ID Number",
                                           "Kin Number", "Password")
        # Format Our Columns
        self.tree_view_admin.column("#0", width=0, stretch=NO)  # phantom column
        self.tree_view_admin.column("Admin_rights", anchor=W, width=150)
        self.tree_view_admin.column("Name", anchor=W, width=100)
        self.tree_view_admin.column("Surname", anchor=W, width=100)
        self.tree_view_admin.column("Phone Number", anchor=W, width=150)  # phantom column
        self.tree_view_admin.column("ID Number", anchor=W, width=150)
        self.tree_view_admin.column("Kin Number", anchor=W, width=150)
        self.tree_view_admin.column("Password", anchor=W, width=150)
        # Create Headings
        # self.tree_view_admin.heading("#0", text="", anchor=CENTER)
        self.tree_view_admin.heading("Admin_rights", text="Admin Rights", anchor=CENTER)
        self.tree_view_admin.heading("Name", text="Name", anchor=CENTER)
        self.tree_view_admin.heading("Surname", text="Surname", anchor=CENTER)
        self.tree_view_admin.heading("Phone Number", text="Phone Number", anchor=CENTER)
        self.tree_view_admin.heading("ID Number", text="ID Number", anchor=CENTER)
        self.tree_view_admin.heading("Kin Number", text="Kin Number", anchor=CENTER)
        self.tree_view_admin.heading("Password", text="Password", anchor=CENTER)

        self.tree_view_admin.place(x=300, y=200)

        # Algorithm adding data to table
        self.data = DatabaseLifeChoices().select_user()
        self.count = 0

        for record in self.data:
            admin_rights = "NO"
            if record[0] == 1:
                admin_rights = "YES"
            self.tree_view_admin.insert(parent="", index="end", iid=self.count, text="", values=(
             admin_rights,
             record[1],
             record[2],
             record[3],
             record[4],
             record[5],
             record[6],
             record[7],
             record[8]
                                                                                               )
                                        )
            self.count += 1

        # Buttons

        # repeatedly show window on screen
        self.window.mainloop()

    #                                                    END OF CONSTRUCTOR


AdminWindow()
