from tkinter import *
import tkinter.messagebox
import sqlite3
import time
import subprocess

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
    
    def user_exists_check(self):
        """Checks if there are any users in the database and returns
        true if there are users and false if not
        """
        conn = sqlite3.connect("users.db")
        c =conn.cursor()
        
        c.execute("SELECT COUNT(*) FROM user")
        count = c.fetchone()[0] #select first row first column
        
        conn.commit()
        conn.close()
        
        return count > 0
          
    def login(self, username, password):
        """This logs in the user by doing the following:
        Checks if there is an input of username and passowrd first if empty return 0
        if successful username and password found, returns 1
        if unsuccessful returns 2
        """
        
        if not username or not password:
            return 0
        conn = sqlite3.connect("users.db")
        c = conn.cursor()
        
        c.execute("SELECT * FROM user WHERE username = ? AND password = ?", (username, password))
        user = c.fetchone()
        
        if user is not None:
            conn.commit()
            conn.close()
            return 1
        else:
            conn.commit()
            conn.close()
            return 2

class books_database_logic:
    """Saves, deletes, updates and checks the database for books"""
    def submit(self, booktitle, author, callnum, callcutter, barcode):
        """Submit takes in the 4 variables and inserts them into the books database"""
        if not booktitle or not author or not callnum or not callcutter or not barcode:
            return 0
        else:
            conn = sqlite3.connect("books.db")
            c = conn.cursor()
            
            insert_books = "INSERT INTO books(booktitle, author, callnum, callcutter, barcode) VALUES(?, ?, ?, ?, ?)"
            c.execute(insert_books, (booktitle, author, callnum, callcutter, barcode))
            
            conn.commit()
            conn.close()
            
            return 1
    
    def book_name(self):
        """Selects specific data from the database and return the value"""
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        
        c.execute("SELECT booktitle FROM books ORDER BY bookID DESC LIMIT 1")
        
        for value in c.fetchall():
            values = value[0]
        
        conn.commit()
        conn.close()
        
        return values
    
    def book_author(self):
        """Selects specific data from the database and return the value"""
        conn = sqlite3.connect("books.db")
        c = conn.cursor()
        
        c.execute("SELECT author FROM books ORDER BY bookID DESC LIMIT 1")
        
       # value = c.fetchone()
        #values = str(value)
        
        for value in c.fetchall():
            values = value[0]
        
        conn.commit()
        conn.close()
        
        return values
        