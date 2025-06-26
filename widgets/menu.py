# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-gui-tkinter/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 6. Menu
# Used to have different pages in the interface (useful for Help and FAQ pages)
# Make the main menu (will contain the other menus inside of it)
menu = tk.Menu(main_window)
# Configure the main window to have the menu
main_window.config(menu=menu)

# Make the file menu
file_menu = tk.Menu(menu)
# Add the file menu to the main menu
menu.add_cascade(label='File', menu=file_menu)
# Set the options for the file menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
# Separator is used to draw a line and write other commands underneath 
# Here, using standard option of 'Exit'
file_menu.add_separator()
file_menu.add_command(label='Exit', command=main_window.quit)

# Make the help menu
help_menu = tk.Menu(menu)
# Add the help menu to the main menu
menu.add_cascade(label='Help', menu = help_menu)
# Set the options for the help menu
help_menu.add_command(label='About')

# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()

