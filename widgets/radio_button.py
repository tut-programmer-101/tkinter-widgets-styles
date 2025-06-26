# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-gui-tkinter/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 4. Radio Button
# Lets the user choose one option from a set of choices 

# Define the type of the variable
choice_type = tk.IntVar()

# Make the radio buttons
# Value is useful when processing the entry choices 
# Anchor is used to position a widget when using pack
# W means West (so will make the entries to the left of the window)
tk.Radiobutton(main_window, text='Yes', value = 1).pack(anchor=tk.W)
tk.Radiobutton(main_window, text='No', value = 2).pack(anchor=tk.W)



# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()

