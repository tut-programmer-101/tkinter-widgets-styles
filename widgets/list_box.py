# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-gui-tkinter/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 5. Listbox
# Lets the user choose one option from a list of options
# Make the listbox 
list_box = tk.Listbox(main_window)
# Set the options
list_box.insert(1, 'Python')
list_box.insert(2, 'Java')
list_box.insert(3, 'C++')
list_box.insert(4, 'Other')
# Call pack 
list_box.pack()


# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()

