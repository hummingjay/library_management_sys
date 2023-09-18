import tkinter as tk

class Next:
    def go_to_next_element(event):
        event.widget.tk_focusNext().focus()

# Create the main window
window = tk.Tk()
window.title("PythonExamples.org")
window.geometry("300x200")

label = tk.Label(window, text="Enter first input")
label.pack()

# First Entry widget
entry_1 = tk.Entry(window)
entry_1.bind('<Return>', Next.go_to_next_element)
entry_1.pack()

label = tk.Label(window, text="Enter second input")
label.pack()

# Second Entry widget
entry_2 = tk.Entry(window)
entry_2.bind('<Return>', Next.go_to_next_element)
entry_2.pack()

# Run the application
window.mainloop()