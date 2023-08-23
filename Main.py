import customtkinter
#import loginv2
from tkinter import *

class leftframe(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        

class topframe(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        
class App(customtkinter.CTk):
    """Main instance of the App"""
    def __init__(self):
        super().__init__()
        
        customtkinter.set_default_color_theme("blue")
        
        self.leftframe = leftframe(self)
        self.leftframe.pack(side=LEFT)
        
        self.topframe = topframe(self)
        self.topframe.pack(side=TOP)
        
app = App()
app.mainloop()