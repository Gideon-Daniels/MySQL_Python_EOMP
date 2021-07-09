from tkinter import *
from tkinter import messagebox
from PIL import *
from connect_to_database import DatabaseLifeChoices
import datetime

# Function to round time in date time class


def round_seconds(time_object):
    try:
        new_time = time_object
        if new_time.microsecond >= 500000:
            new_time = new_time + datetime.timedelta(seconds=1)
            return new_time.replace(microsecond=0)
    except TypeError:
        messagebox.showerror("system Error", "please try again")


def current_date():
    date = datetime.date.today()
    return date


def current_time():
    time = datetime.datetime.today().time()
    rounded_time = round_seconds(time)
    return rounded_time


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
        for data in self.attendance:
            if self.entry_password.get() == "" or self.entry_username.get() == "":
                messagebox.showinfo("INVALID", "Username or Password is incorrect")
                break
            else:
                for record in self.login_details:
                    if data[3] != 0 and record[2] == self.entry_password.get() and record[1] == \
                            self.entry_username.get():
                        messagebox.showinfo("INFO", "You have already signed in")
                        break
                    elif record[2] == self.entry_password.get() and record[1] == self.entry_username.get():
                        date_stamp = current_date()
                        time_stamp = current_time()
                        DatabaseLifeChoices().insert_attendance_register(record[0], record[1], date_stamp, time_stamp, 0)
                        messagebox.showinfo("Successful", "LOGIN SUCCESSFUL")
                        break
                    else:
                        messagebox.showinfo("INVALID", "Username or Password is incorrect")
                        break
                break

    def sign_out(self):
        for record in self.attendance:
            if record[4] == 0 and record[1] == self.entry_username.get() and record[2] == self.entry_password.get():
                sign_out_time = current_time()
                DatabaseLifeChoices().update_attendance_register(record[3], sign_out_time)
                break
            elif record[4] != 0 and record[1] == self.entry_username.get() and record[2] == self.entry_password.get():
                messagebox.showinfo("INFO", "YOU HAVE ALREADY SIGNED OUT")
                break
            else:
                messagebox.showinfo("INVALID", "Username or Password is incorrect")
                break

    def registration_window(self):
        self.window.destroy()
        import Registration_window

    def exit_window(self):
        self.window.destroy()


Login()
