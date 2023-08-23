import tkinter as tk

root = tk.Tk()

# Create the menu bar
menubar = tk.Menu(root)

# Create the File menu
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
filemenu.add_separator()
filemenu.add_command(label="Exit")

# Create the Expandable menu
expandablemenu = tk.Menu(menubar, tearoff=0)
expandablemenu.add_command(label="Option 1")
expandablemenu.add_command(label="Option 2")
expandablemenu.add_command(label="Option 3")

# Add the menus to the menu bar
menubar.add_cascade(label="File", menu=filemenu)
menubar.add_cascade(label="Expandable", menu=expandablemenu)

# Pack the menu bar
menubar.pack(side=tk.LEFT, fill=tk.Y)

root.mainloop()
