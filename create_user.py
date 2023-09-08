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

conn.commit()
conn.close()

class inputframe(customtkinter.CTkFrame):
    """Sets up up the frame for the login buttons and entry boxes"""
    def __init__(self, master):
        super().__init__(master)
        
        self.label =customtkinter.CTkLabel(self, text="Create user", font=("Helvetica", 28))
        self.label.grid(row=0, column=0, pady=12, padx=10)
        
        # inputs
        self.user = customtkinter.CTkEntry(self, placeholder_text="Username")
        self.user.grid(row=1, column=0, pady=12, padx=10)
        self.passwd = customtkinter.CTkEntry(self, placeholder_text="Password", show="*")
        self.passwd.grid(row=2,column=0, pady=12, padx=10)
        self.repasswd = customtkinter.CTkEntry(self, placeholder_text="re-enter password")
        self.repasswd.grid(row=3, column=0, pady=12, padx=10)
        
        #create user button
        self.button = customtkinter.CTkButton(self, text="Create me", command=self.create_user, font=("gothic", 21))
        self.button.grid(row=4, column=0, pady=12, padx=10)
        
    def create_user(self):
        """ Loging the user into the system and destroying login page to Main.py"""
        username = self.user.get()
        password = self.passwd.get()
        repassword = self.repasswd.get()
        
        results = process_logic.login_logic.create_new_user(self, username, password, repassword)
        
        if results == 2:
            messagebox.showerror("Login failure", "Invalid username or password")
        elif results == 0:
              messagebox.showinfo("Login requirements", "Input username and password")
        else:
            self.destroy()
    
class App(customtkinter.CTk):
    """Main app for running login page Accesese the frames and defines the geometry of login page"""
    def __init__(self):
        super().__init__()
        
        self.title("Create User")
        self.geometry("600x400")
        self.iconbitmap("images/login.ico")
        
        customtkinter.set_appearance_mode("system")
        customtkinter.set_default_color_theme("blue")
        
    
        #input call
        self.inputframe = inputframe(self)
        self.inputframe.pack(side = LEFT, fill=BOTH)
       

if __name__ == "__main__":
    app = App()
    app.mainloop()