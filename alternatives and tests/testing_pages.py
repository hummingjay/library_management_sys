import customtkinter
import sqlite3
from tkinter import *

conn = sqlite3.connect("books.db")
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books(
    bookID INTEGER PRIMARY KEY,
    booktitle VARCHAR(49) NOT NULL,
    author VARCHAR(49) NOT NULL,
    availability VARCHAR(7) Default 'YES',
    callnum VARCHAR(21) NOT NULL,
    callcutter VARCHAR(7) NOT NULL,
    barcode VARCHAR(14) Default '69420')
    ''')

conn.commit()
conn.close()

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

class sideframe(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=140, corner_radius=7)
        self.the_label = customtkinter.CTkLabel(self, text="My Library", font=("Helvetica", 14))
        self.the_label.grid(row=0, column=0, padx=20, pady=10)

        # Buttons for switching between pages
        self.home_btn = customtkinter.CTkButton(self, text="Home", font=("Helvetica", 21), command=master.show_home)
        self.home_btn.grid(row=1, column=0, padx=21, pady=14)

        self.catalogbtn = customtkinter.CTkButton(self, text="Catalog", command=master.show_catalog)
        self.catalogbtn.grid(row=2, column=0, padx=10, pady=20)

        self.adduserbtn = customtkinter.CTkButton(self, text="Add User", command=master.show_add_user)
        self.adduserbtn.grid(row=3, column=0, padx=20, pady=10)

        self.circulate = customtkinter.CTkButton(self, text="Circulation", command=master.show_circulation)
        self.circulate.grid(row=4, column=0, padx=20, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self, text="Appearance Mode:")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=10)

        self.appearance_mode_size_label = customtkinter.CTkLabel(self, text="Zoom")
        self.appearance_mode_size_label.grid(row=7, column=0)

        self.appearance_mode_size = customtkinter.CTkOptionMenu(self, values=["50", "60", "70", "80", "90", "100", "110", "120", "130"],
                                                                command=self.change_scaling_event)
        self.appearance_mode_size.grid(row=8, column=0, padx=20, pady=10)

        self.appearance_mode_color_label = customtkinter.CTkLabel(self, text="Color mode")
        self.appearance_mode_color_label.grid(row=9, column=0)

        self.appearance_mode_color = customtkinter.CTkOptionMenu(self, values=["Dark", "System", "Light"],
                                                                 command=self.change_appearance_mode_event)
        self.appearance_mode_color.grid(row=10, column=0, padx=20, pady=10)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        """Sets the app into light, dark or system mode"""
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        """"Resizes the app widgets to zoom in and out for easy view"""
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

class resultframe(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")

    def clear_content(self):
        for widget in self.winfo_children():
            widget.destroy()

class App(customtkinter.CTk):
    """Main instance of the App"""
    def __init__(self):
        super().__init__()

        self.title("Library Management system")
        self.geometry("770x700")
        self.iconbitmap("images/login.ico")

        # dictionary to map pages to their corresponding frame
        self.pages = {
            "home": self.create_home,
            "catalog": self.create_catalog,
            "add_user": self.create_add_user,
            "circulation": self.create_circulation
        }

        # configuring the grid layout
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        #self.grid_rowconfigure((0, 1, 2), weight=1)

        # calling frames
        self.sideframe = sideframe(self)
        self.sideframe.grid(row=0, rowspan=4, column=0, sticky="wens")
        self.grid_rowconfigure(3, weight=1)
        self.search_bar = customtkinter.CTkEntry(self, placeholder_text="Search")
        self.search_bar.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20,20), sticky="nsew")
        self.search_bar_button = customtkinter.CTkButton(self, text="Search", command=self.search, fg_color="brown", hover_color="brown1")
        self.search_bar_button.grid(row=0, column=3)
        self.resultframe = resultframe(self)
        self.resultframe.grid(row=1, rowspan=3, column=1, columnspan=3, sticky="wens")

        # setting defaults
        self.sideframe.appearance_mode_size.set("100%")
        self.sideframe.appearance_mode_color.set("System")

        # Initially, show the "Home" page
        self.show_home()

    def clear_resultframe(self):
        self.resultframe.clear_content()

    def show_home(self):
        self.clear_resultframe()
        self.pages["home"]()

    def create_home(self):
        home_label = customtkinter.CTkLabel(self.resultframe, text="Home")
        home_label.pack()

    def search(self):
        pass

    def show_catalog(self):
        self.clear_resultframe()
        self.pages["catalog"]()

    def create_catalog(self):
        catalog_label = customtkinter.CTkLabel(self.resultframe, text="Catalog")
        catalog_label.pack()

    def show_add_user(self):
        self.clear_resultframe()
        self.pages["add_user"]()

    def create_add_user(self):
        add_user_label = customtkinter.CTkLabel(self.resultframe, text="Add User")
        add_user_label.pack()

    def show_circulation(self):
        self.clear_resultframe()
        self.pages["circulation"]()

    def create_circulation(self):
        circulation_label = customtkinter.CTkLabel(self.resultframe, text="Circulation")
        circulation_label.pack()

app = App()
app.mainloop()
