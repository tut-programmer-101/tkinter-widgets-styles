# Adapted from GeeksforGeeks: https://www.geeksforgeeks.org/python/python-tkinter-text-widget/

# Import the tkinter library
import tkinter as tk

# Use the Tk class to make a main window
main_window = tk.Tk()

# Make a title for the window 
main_window.title('Coding Project')


### WIDGETS (COMPONENTS) ###

# 7. Text Widget
# We can use text widgets to print sentences or blocks of text
# Create text widget and specify the size (height and width)
text_widget = tk.Text(main_window, height = 5, width = 60)
game_title = tk.Label(main_window, text="Game Name")
game_intro = """
Welcome to <Game Name>! These are the rules of the game 
1. Try to collect as many coins as you can. 
2. You only have 60 seconds. 
3. The score to beat is 20.
"""

# Pack the widgets
game_title.pack()
text_widget.pack()
# Insert the text into the text widget
text_widget.insert(tk.END, game_intro)


# Run the application
# Sets up an infinite loop which makes the application run
# This line always has to go at the end of the code
main_window.mainloop()




