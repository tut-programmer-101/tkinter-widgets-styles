# Adapted from GeeksforGeeks

# Widget code adapted from GeeksforGeeks: 
# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 2. Button
# Width sets the width of the button in pixels
# Destroy will close the interface
button = tk.Button(main_window, text='Close', width = 25, command=main_window.destroy)
button.pack()


# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()


