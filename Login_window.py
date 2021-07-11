from tkinter import *
from tkinter import messagebox
from PIL import *
from connect_to_database import DatabaseLifeChoices
import datetime


# Function to round time in date time class


def current_date():
    date = datetime.date.today()
    return date


def current_time():
    time = datetime.datetime.today().time()
    return time


class Login:
    def __init__(self):
        # creating window
        self.window = Tk()
        self.window.title("Login Page")
        self.window.geometry("400x500")
        self.window.config(bg="#323232")

        # creating widgets
        # Labels
        self.label_username = Label(self.window, text="USERNAME", )
        self.label_username.config(font="Arial 16 bold", bg="#323232", fg="#78cc6d")
        self.label_username.place(y=100, x=50)

        self.label_password = Label(self.window, text="PASSWORD", )
        self.label_password.config(font="Arial 16 bold", bg="#323232", fg="#78cc6d")
        self.label_password.place(y=150, x=50)
        # Entries
        self.entry_username = Entry(self.window, )
        self.entry_username.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_username.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_username.place(y=100, x=200)

        self.entry_password = Entry(self.window, )
        self.entry_password.config(highlightthickness=3, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.entry_password.config(width=15, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.entry_password.place(y=150, x=200)
        # Buttons
        self.button_login = Button(self.window, text="Login", command=self.login_button)
        self.button_login.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_login.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_login.place(y=250, x=50)

        self.button_register = Button(self.window, text="Register", command=self.registration_window)
        self.button_register.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_register.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_register.place(y=250, x=250)

        self.button_logout = Button(self.window, text="Log out", command=self.sign_out)
        self.button_logout.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_logout.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_logout.place(y=300, x=50)

        self.button_exit = Button(self.window, text="Exit", command=self.exit_window)
        self.button_exit.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_exit.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_exit.place(y=300, x=250)

        # fetching data from database
        self.login_details = DatabaseLifeChoices().select_log_in_details()
        self.attendance = DatabaseLifeChoices().select_attendance_register()
        # Images

        # repeatedly show window on screen
        self.window.mainloop()

    #                                                     ALL FUNCTIONS

    def login_button(self):
        try:
            for data in self.attendance:
                for record in self.login_details:
                    if self.entry_password.get() == "" or self.entry_username.get() == "":
                        messagebox.showinfo("INVALID", "Username or Password is incorrect")
                        break
                    elif data[4] == 0 and record[2] == self.entry_password.get() and record[1] == \
                            self.entry_username.get():
                        messagebox.showinfo("INFO", "You have already signed in")
                        break
                    elif record[2] == self.entry_password.get() and record[1] == self.entry_username.get():
                            date_stamp = current_date()
                            time_stamp = datetime.datetime.today().time()
                            print(time_stamp)
                            DatabaseLifeChoices().insert_attendance_register(record[0], record[1], date_stamp,
                                                                             time_stamp, 0)
                            messagebox.showinfo("Successful", "LOGIN SUCCESSFUL")
                            break
        except:
            messagebox.showinfo("SYSTERM ERROR","CONTACT ADMIN FOR MORE INFO")
        else:
            messagebox.showinfo("INVALID", "USERNAME OR PASSWORD INCORRECT!")

    def sign_out(self):
        for data_in_attendance in self.attendance:
            if self.entry_password.get() == "" or self.entry_username.get() == "":
                messagebox.showinfo("INVALID", "Username or Password is incorrect")
                break
            else:
                for record in self.login_details:
                    if data_in_attendance[4] == datetime.timedelta(0) and record[2] == self.entry_password.get() and \
                            record[1] == self.entry_username.get():
                        time_stamp = current_time()
                        DatabaseLifeChoices().update_attendance_register(data_in_attendance[2], time_stamp)
                        messagebox.showinfo("Successful", "LOG OUT SUCCESSFUL")
                        break
                    elif data_in_attendance[4] != datetime.timedelta(0) and record[2] == self.entry_password.get() and \
                            record[1] == self.entry_username.get():
                        messagebox.showinfo("INFO", "YOU ARE ALREADY LOGGED OUT")

                break

    def registration_window(self):
        self.window.destroy()
        import Registration_window

    def exit_window(self):
        self.window.destroy()


Login()
