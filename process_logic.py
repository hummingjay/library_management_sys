from tkinter import *
import tkinter.messagebox
import sqlite3
import time


class login_logic:
    """Defines the different login methods and user checks for the system"""
    def create_new_user(self, username, password, repassword):
        """This checks if a user exists before creating a new user"""
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        
        while True:
            find_user = ("SELECT * FROM user WHERE username = ?")
            c.execute(find_user, [(username)])
            if (c.fetchall()):
                tkinter.messagebox.showerror("User name", "User name exists")
            else:
                break
        while password != repassword:
            tkinter.messagebox.showerror("Password", "password mismatch")
        insert = "INSERT INTO user(username, password) VALUES(?, ?)"
        c.execute(insert, [(username), (password)])
        
        conn.commit()
        conn.close()
        
        time.sleep(2)
        return
    
    #def database_check(self):
          
    def login(self, username, password):
        conn = sqlite3.connect("usersLibrary_management.db")
        c = conn.cursor()
        
        c.execute
        
        conn.commit()
        conn.close()