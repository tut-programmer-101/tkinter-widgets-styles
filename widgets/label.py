# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-gui-tkinter/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 1. Label
# Will show the text we choose
label = tk.Label(main_window, text='Coding Project')
# Pack organises widget
# Can also use grid (rows and columns), place (for x,y coordinates) - need to be consistent
# i.e. use the same one throughout. Here we will use pack
label.pack()


# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()


