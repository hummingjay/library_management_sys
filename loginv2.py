from tkinter import *
import customtkinter
import sqlite3
from tkinter import messagebox
import process_logic

conn = sqlite3.connect("users.db")
c =conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS user(
    userID INTEGER PRIMARY KEY,
    username VARCHAR(20) NOT NULL,
    password VARCHAR(20) NOT NULL)
    ''')

class inputframe(customtkinter.CTkFrame):
    """Sets up up the frame for the login"""
    def __init__(self, master):
        super().__init__(master)
        
        self.label =customtkinter.CTkLabel(self, text="User Login", font=("Helvetica", 28))
        self.label.grid(row=0, column=0, pady=12, padx=10)
        
        # inputs
        self.user = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.user.grid(row=1, column=0, pady=12, padx=10)
        self.passwd = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwd.grid(row=2,column=0, pady=12, padx=10)
        
        #login button
        self.button = customtkinter.CTkButton(self, text="Login", command=App.log_in)
        self.button.grid(row=3, column=0, pady=12, padx=10)
        
        self.checkbox = customtkinter.CTkCheckBox(self, text="Remember Me")
        self.checkbox.grid(row=4, column=0, pady=12, padx=10)
    
class App(customtkinter.CTk):
    """Main app for running login page"""
    def __init__(self):
        super().__init__()
        
        self.title("Login Page")
        self.geometry("770x700")
        self.iconbitmap("login.ico")
        
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")
        
    
        #input call
        self.inputframe = inputframe(self)
        self.inputframe.pack(side = LEFT, fill=BOTH)
        
    def log_in(self):
        """ Loging the user into the system"""
        username = self.user.get()
        password = self.passwd.get()
        
        results = process_logic.login_logic.login(username, password)
        
        if results == 1:
            messagebox.showerror("Login failure", "Invalid username or password")
        else:
            import Main

if __name__ == "__main__":
    app = App()
    app.mainloop()