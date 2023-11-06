import tkinter as tk

def insert_text():
    # Get the text to be inserted from an Entry widget
    text_to_insert = entry_text.get()
    
    # Insert the text at the beginning (0) of the Entry widget
    entry_widget.insert(0, text_to_insert)

# Create a Tkinter window
root = tk.Tk()
root.title("Entry Insert Example")

# Create an Entry widget
entry_text = tk.Entry(root)
entry_text.pack()

# Create a Button that inserts text into the Entry widget
insert_button = tk.Button(root, text="Insert Text", command=insert_text)
insert_button.pack()

# Create another Entry widget to show the inserted text
entry_widget = tk.Entry(root)
entry_widget.pack()

root.mainloop()
