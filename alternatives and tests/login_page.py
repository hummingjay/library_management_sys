import customtkinter
import mysql.connector

"""
    This is the login page for the library management sytem
"""

#setting appearance and theme
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

#the appliction 
root = customtkinter.CTk()
root.geometry("600x400")
root.title("Login page")

#icon in title bar
root.iconbitmap('images/login.ico')

def login():
    """Logs the user into the system"""
    username = entry1.get()
    password = entry2.get()
    
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="my_database"
    )
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    
    results = cursor.fetchall()
    
    if len(results) == 0:
        print("Invalid username or passsword.")
    else:
        print("Login successful.")
    
    cursor.close()
    connection.close()

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="User Login", font=("Helvetica", 28))
label.pack(pady=12, padx=10)

#inputs
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()