import customtkinter
import process_logic
from tkinter import *
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect("books.db")
c =conn.cursor()

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
        
        self.home_btn = customtkinter.CTkButton(self, text="Home",font=("Helvetica", 21), command=master.show_home)
        self.home_btn.grid(row=1, column=0, padx=21, pady=14)
        
        self.catalogbtn = customtkinter.CTkButton(self, text="Catalog", command=master.show_catalog)
        self.catalogbtn.grid(row=2, column=0, padx=10, pady=20)
        
        self.adduserbtn =customtkinter.CTkButton(self, text="Add User", command=master.show_add_user)
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
            "home": self.home,
            "catalog": self.catalog,
            "add_user": self.add_user,
            "circulation": self.circulation,
            "search": self.search
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
        self.search_bar.grid(row=0, column=1, columnspan=2, padx=(20, 5), pady=(20,20), sticky="nsew")
        self.search_bar_button = customtkinter.CTkButton(self, text="Search", command=self.show_search, fg_color="brown", hover_color="brown1")
        self.search_bar_button.grid(row=0, column=3)
        self.resultframe = resultframe(self)
        self.resultframe.grid(row=1, rowspan=3, column=1, columnspan=3, sticky="wens")
        
        #setting defaults
        self.sideframe.appearance_mode_size.set("100%")
        self.sideframe.appearance_mode_color.set("System")
        
        #initial page to be shown
        self.show_home()
    
    def clear_resultframe(self):
        self.resultframe.clear_content()
    
    # functions for home
    def show_home(self):
        self.clear_resultframe()
        self.pages["home"]()
        
    def home(self):
        home_label = customtkinter.CTkLabel(self.resultframe, text="Home", font=("helvetica", 28))
        home_label.grid(row=0, column=0, padx=20, pady=10)
        
        recent_books = customtkinter.CTkLabel(self.resultframe, text="Recent Books:", font=("helvetica", 14))
        recent_books.grid(row=1, column=0, padx=20, pady=10)
        
        book_name_tile = customtkinter.CTkLabel(self.resultframe, text="Book")
        book_name_tile.grid(row=2, column=0, padx=20, pady=10)
        
        b_name = process_logic.books_database_logic.book_name(self)
        
        book_name = customtkinter.CTkLabel(self.resultframe, text=b_name)
        book_name.grid(row=3, column=0, padx=20, pady=10)
        
        book_author_tile = customtkinter.CTkLabel(self.resultframe, text="Author")
        book_author_tile.grid(row=2, column=1, padx=20, pady=10)
        
        a_name = process_logic.books_database_logic.book_author(self)
        
        book_author = customtkinter.CTkLabel(self.resultframe, text=a_name)
        book_author.grid(row=3, column=1, padx=20, pady=10)
        
        
        
    
    # functions for search
    def search(self):
        home_label = customtkinter.CTkLabel(self.resultframe, text="Search Results:", font=("helvetica", 28))
        home_label.grid(row=0, column=0, padx=20, pady=10)
    
    def show_search(self):
        self.clear_resultframe()
        self.pages["search"]()
    
    #functions for catalog
    def catalog(self):
        self.resultframe.grid_columnconfigure((1, 2), weight=1)
        self.resultframe.grid_columnconfigure((2, 3), weight=0)
        
        # Labels
        catalog_label = customtkinter.CTkLabel(self.resultframe, text="Catalogue", font=("helvetica", 28))
        catalog_label.grid(row=0, column=0, padx=20, pady=10)
        
        Book_title_label =customtkinter.CTkLabel(self.resultframe, text="Book Name:", font=("Helvetica", 14))
        Book_title_label.grid(row=1, column=0)
        
        author_name_label = customtkinter.CTkLabel(self.resultframe, text="Author:",font=("Helvetica", 14))
        author_name_label.grid(row=2, column=0)
        
        call_number_label =customtkinter.CTkLabel(self.resultframe, text="Call Number:", font=("Helvetica", 14))
        call_number_label.grid(row=3, column=0)
        
        call_cutter_label = customtkinter.CTkLabel(self.resultframe, text="Call Cutter:",font=("Helvetica", 14))
        call_cutter_label.grid(row=4, column=0)
        
        lib_serial_label = customtkinter.CTkLabel(self.resultframe, text="Barcode:",font=("Helvetica", 14))
        lib_serial_label.grid(row=5, column=0)
        
        # define Entries
        Book_title = customtkinter.CTkEntry(self.resultframe, placeholder_text="Book Title")
        Book_title.grid(row=1, column=1, columnspan=2, padx=(5, 5), pady=(20,20), sticky="nsew")
        
        author_name = customtkinter.CTkEntry(self.resultframe, placeholder_text="Author")
        author_name.grid(row=2, column=1, columnspan=2, padx=(5, 5), pady=(20, 20), sticky="news")
        
        call_number = customtkinter.CTkEntry(self.resultframe, placeholder_text="Call Number")
        call_number.grid(row=3, column=1, columnspan=2, padx=(5, 5), pady=(20,20), sticky="nsew")
        
        call_cutter = customtkinter.CTkEntry(self.resultframe, placeholder_text="Call Cutter")
        call_cutter.grid(row=4, column=1, columnspan=2, padx=(5, 5), pady=(20, 20), sticky="news")
        
        lib_serial = customtkinter.CTkEntry(self.resultframe, placeholder_text="eg:123456789")
        lib_serial.grid(row=5, column=1, columnspan=2, padx=(5, 5), pady=(20, 20), sticky="news")
        
        #submission defination and picking
        def submit_catalog():
            booktitle = Book_title.get()
            author = author_name.get()
            callnum = call_number.get()
            callcutter = call_cutter.get()
            barcode = lib_serial.get()
            
            submission = process_logic.books_database_logic.submit(self, booktitle, author, callnum, callcutter, barcode)
            
            if submission == 0:
                messagebox.showerror("Empty inputs", "Please input all required values")
            else:
                self.show_home
        
        submit_btn = customtkinter.CTkButton(self.resultframe, text="Submit", command=submit_catalog)
        submit_btn.grid(row=6, column=2, padx=(5,5))
    
    def show_catalog(self):
        self.clear_resultframe()
        self.pages["catalog"]()
    
    #functions for adding user
    def add_user(self):
        add_user_label = customtkinter.CTkLabel(self.resultframe, text="Add Patron", font=("helvetica", 28))
        add_user_label.grid(row=0, column=0, padx=20, pady=10)
    
    def show_add_user(self):
        self.clear_resultframe()
        self.pages["add_user"]()
    
    # functions for circulation
    def circulation(self):
        circulation_label = customtkinter.CTkLabel(self.resultframe, text="Circulation", font=("helvetica", 28))
        circulation_label.grid(row=0, column=0, padx=20, pady=10)
    
    def show_circulation(self):
        self.clear_resultframe()
        self.pages["circulation"]()
    
    
if __name__ == "__main__":
    app = App()
    app.mainloop()