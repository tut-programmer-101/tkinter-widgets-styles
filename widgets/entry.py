# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-gui-tkinter/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 3. Entry 
# Takes in a single line of text as user input 

# The screen can have more than one entry (here we will make two)
# Notice there is no button in this example - a button is needed to process or save the inputs
# in the Python code

# Make the label for both entries
tk.Label(main_window, text = 'First Name').grid(row = 0)
tk.Label(main_window, text = 'Last Name').grid(row = 1)
# Make the two entries 
entry_one = tk.Entry(main_window)
entry_two = tk.Entry(main_window)
# Position the entries in a grid (with two rows and one column)
entry_one.grid(row = 0, column = 1)
entry_two.grid(row = 1, column = 1)


# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()

