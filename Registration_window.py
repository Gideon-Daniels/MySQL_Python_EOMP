from tkinter import *
from tkinter import messagebox
from connect_to_database import DatabaseLifeChoices


class Registration:
    def __init__(self):
        # creating window
        self.window = Tk()
        self.window.title("Login Page")
        self.window.geometry("720x720")
        self.window.config(bg="#323232")

        # creating widgets
        # Frames
        self.frame_header = Frame(self.window, width=100, height=100, bg="#78cc6d")
        self.frame_header.pack(fill="both")
        self.frame_details = Frame(self.window, width=600, height=440, bg="#78cc6d")
        self.frame_details.place(x=60, y=120)
        self.frame_footer = Frame(self.window, width=100, height=100, bg="#78cc6d")
        self.frame_footer.pack(fill="both", side="bottom")

        # Labels
        #                                 LABEL FOR HEADER FRAME
        self.label_header_one = Label(self.frame_header, text="LIFE CHOICES")
        self.label_header_one.place(x=300)
        self.label_header_one.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")
        self.label_header_two = Label(self.frame_header, text="REGISTRATION")
        self.label_header_two.place(y=50, x=300)
        self.label_header_two.config(font="Arial 20 bold", bg="#78cc6d", fg="#323232")

        #                                LABEL FOR DETAILS FRAME
        self.label_personal_details = Label(self.frame_details, text="PERSONAL DETAILS")
        self.label_personal_details.config(font="Arial 20 bold", fg="#78cc6d", bg="#323232", width=50)
        self.label_personal_details.place(x=-30, y=5)
        self.label_next_of_kin_details = Label(self.frame_details, text="NEXT OF KIN")
        self.label_next_of_kin_details.config(font="Arial 20 bold", fg="#78cc6d", bg="#323232", width=50)
        self.label_next_of_kin_details.place(x=-30, y=180)
        self.label_login_details = Label(self.frame_details, text="LOGIN DETAILS", width=50)
        self.label_login_details.config(font="Arial 20 bold", fg="#78cc6d", bg="#323232")
        self.label_login_details.place(x=-30, y=300)
        #                        DESCRIPTION LABELS FOR PERSONAL DETAILS
        self.label_name = Label(self.frame_details, text="NAME")
        self.label_name.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_name.place(x=20, y=50)

        self.label_surname = Label(self.frame_details, text="SURNAME")
        self.label_surname.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_surname.place(x=20, y=100)

        self.label_id_num = Label(self.frame_details, text="ID NUM")
        self.label_id_num.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_id_num.place(x=300, y=50)

        self.label_cell_num = Label(self.frame_details, text="CELL NUM")
        self.label_cell_num.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_cell_num.place(x=300, y=100)
        #                        DESCRIPTION LABELS FOR NEXT OF KIN
        self.label_kin_name = Label(self.frame_details, text="NAME")
        self.label_kin_name.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_kin_name.place(x=30, y=245)

        self.label_kin_cell_num = Label(self.frame_details, text="CELL NUM")
        self.label_kin_cell_num.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_kin_cell_num.place(x=300, y=245)
        #                        DESCRIPTION LABELS FOR LOGIN DETAILS
        self.label_username = Label(self.frame_details, text="USERNAME")
        self.label_username.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_username.place(x=30, y=370)

        self.label_password = Label(self.frame_details, text="PASSWORD")
        self.label_password.config(font="Arial 16 bold", bg="#78cc6d", fg="#323232")
        self.label_password.place(x=300, y=370)
        # Entries
        #                  ENTRIES FOR PERSONAL DETAILS
        self.entry_name = Entry(self.frame_details)
        self.entry_name.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_name.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_name.place(x=150, y=50)

        self.entry_surname = Entry(self.frame_details)
        self.entry_surname.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_surname.config(width=15, font="Arial 12", bg="#323232", fg="#78cc6d")
        self.entry_surname.place(x=150, y=100)

        self.entry_id_num = Entry(self.frame_details)
        self.entry_id_num.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_id_num.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_id_num.place(x=450, y=50)

        self.entry_cell_num = Entry(self.frame_details)
        self.entry_cell_num.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_cell_num.config(width=15, font="Arial 12", bg="#323232", fg="#78cc6d")
        self.entry_cell_num.place(x=450, y=100)

        #                  ENTRIES FOR NEXT OF KIN
        self.entry_kin_name = Entry(self.frame_details)
        self.entry_kin_name.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_kin_name.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_kin_name.place(x=150, y=245)

        self.entry_kin_cell_num = Entry(self.frame_details)
        self.entry_kin_cell_num.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_kin_cell_num.config(width=15, font="Arial 12", bg="#323232", fg="#78cc6d")
        self.entry_kin_cell_num.place(x=450, y=245)

        #                  ENTRIES FOR LOGIN DETAILS
        self.entry_username = Entry(self.frame_details)
        self.entry_username.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_username.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_username.place(x=150, y=370)

        self.entry_password = Entry(self.frame_details)
        self.entry_password.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_password.config(width=15, font="Arial 12", bg="#323232", fg="#78cc6d")
        self.entry_password.place(x=450, y=370)
        # Buttons
        self.button_exit = Button(self.window, text="Exit", command=self.exit_window)
        self.button_exit.config(width=10, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_exit.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_exit.place(y=580, x=450)

        self.button_register = Button(self.window, text="Register", command=self.register_information)
        self.button_register.config(width=10, font="Arial 12 ", fg="#323232", bg="#78cc6d")
        self.button_register.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_register.place(y=580, x=250)

        # repeatedly show window on screen
        self.window.mainloop()

    def register_information(self):
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        id_number = self.entry_id_num.get()
        cell_num = self.entry_cell_num.get()
        kin_name = self.entry_kin_name.get()
        kin_cell_num = self.entry_kin_cell_num.get()
        username = self.entry_username
        password = self.entry_password

        if username == "" or \
                password == "" or \
                name == "" or \
                surname == "" or \
                id_number == "" or \
                kin_name == "" or \
                kin_cell_num == "" \
                or cell_num == "":
            messagebox.showinfo("INVALID FIELDS", "Please fill in all fields")
        elif len(id_number) > 13:
            messagebox.showinfo("INVALID ID", "PLEASE ENTER 13 DIGIT ID")
        elif len(cell_num) > 10 and not str(cell_num).isdigit() and len(kin_cell_num) > 10\
                and not str(kin_cell_num).isdigit():
            messagebox.showinfo("INVALID CELL NUMBER", "PLEASE ENTER VALID CELL NUMBERS")
        elif any(map(str.isdigit, name)) and any(map(str.isdigit, surname) and any(map(str.isdigit, kin_name))):  #
            # checks if name or name has a has an integer
            messagebox.showinfo("INVALID NAME OR SURNAME", "Please enter a name without any numbers")
        else:
            DatabaseLifeChoices().insert_user(name, surname, cell_num, kin_cell_num, False, password,
                                              id_number)
            self.window.destroy()
            import Login_window

    def exit_window(self):
        self.window.destroy()


Registration()
