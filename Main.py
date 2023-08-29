import customtkinter
#import loginv2
from tkinter import *

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

class sideframe(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=140, corner_radius=7)
        self.the_label = customtkinter.CTkLabel(self, text="My Library", font=("Helvetica", 14))
        self.the_label.grid(row=0, column=0, padx=20, pady=10)
        
        self.searchbtn = customtkinter.CTkButton(self, text="Catalog", command=App.books_view)
        self.searchbtn.grid(row=2, column=0, padx=10, pady=20)
        
        self.adduserbtn =customtkinter.CTkButton(self, text="Add User", command=App.add_user)
        self.adduserbtn.grid(row=3, column=0, padx=20, pady=10)
        
        self.circulate = customtkinter.CTkButton(self, text="Circulation", command=App.circulation)
        self.circulate.grid(row=4, column=0, padx=20, pady=10)
      
class App(customtkinter.CTk):
    """Main instance of the App"""
    def __init__(self):
        super().__init__()
        
        self.title("Library Management system")
        self.geometry("770x700")
        
        # configuring the grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2,3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # calling frames
        self.sideframe = sideframe(self)
        self.sideframe.grid(row=0, rowspan=4, column=0, sticky="wens")
        self.grid_rowconfigure(3, weight=1)
    
    def books_view(self):
        pass
    
    def add_user(self):
        pass
    
    def circulation(self):
        pass
        
if __name__ == "__main__":
    app = App()
    app.mainloop()