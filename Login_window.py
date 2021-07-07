from tkinter import *
from tkinter import messagebox
from PIL import *
from connect_to_database import DatabaseLifeChoices


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
        self.button_login = Button(self.window, text="Register", )
        self.button_login.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_login.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_login.place(y=250, x=250)
        self.button_login = Button(self.window, text="Exit", )
        self.button_login.config(width=10, font="Arial 12 ", bg="#323232", fg="#78cc6d")
        self.button_login.config(highlightthickness=1, highlightbackground="#78cc6d", highlightcolor="#78cc6d")
        self.button_login.place(y=300, x=150)
        # Images

        # repeatedly show window on screen
        self.window.mainloop()

    def login_button(self):
        usernames = DatabaseLifeChoices()


Login()
