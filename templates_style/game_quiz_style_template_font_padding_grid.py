## IMPORTANT: Need to use Ttk widgets, not tk widgets for this to work!
# e.g. ttk.Button(), ttk.Label() etc

## Ttk Themes Documentation: https://ttkthemes.readthedocs.io/en/latest/index.html 
## Adapted from: Tkinter.com, Style And Theme Your App The Easy Way - Tkinter Projects 4
# Import libraries
import tkinter as tk
from tkinter import ttk
from tkinter.constants import * # For left, right, x, y etc
# Import style library themes
from ttkthemes import ThemedTk


# Use ThemedTk for style instead of tk.Tk
class gameApp(ThemedTk):
    def __init__(self, *args, **kwargs):
        ThemedTk.__init__(self, *args, **kwargs)

        # Set the dimensions of the window and make it non-resizable
        self.geometry("600x400")
        # Made the window fixed (to be able to resize, uncommend this line)
        self.resizable(False,False)
        # Set the title of the main window
        self.title("Game Name")

        ## NEW ##
        # Use ttkthemes
        self.set_theme("breeze") # breeze theme

        ## NEW ##
        # Set the background to be the same colour as the theme 
        try:
            # Search for the background
            self.theme_bg = ttk.Style().lookup('TFrame', 'background', default='SystemButtonFace')
        except tk.TclError:
            self.theme_bg = 'SystemButtonFace' # Default if lookup fails 

        # Make a container 
        # Set the background ## NEW ##
        container = tk.Frame(self, bg = self.theme_bg)

        # Pack the container and set to fill the entire window
        container.pack(fill=BOTH, expand = True)

        # Configure container's grid to allow frames to expand within it 
        # This will make each frame fill up the window 
        # Use a grid to ensure each page displays in exact same place on the screen
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)

        # Initialise frames to an empty array
        self.frames = {}

        # Iterate through tuple of the page layouts
        # ## NEW ## Use theme_bg with constructor
        for F in (IntroPage,MainPage,ScorePage):
            frame = F(container, self, theme_bg = self.theme_bg)
            # Initialise the frame 
            self.frames[F] = frame
            # Place the frame in the container's grid, to exist in the same cell
            # This will stack the pages in front of one another
            frame.grid(row=0,column=0,sticky=NSEW)
        
        # Shoe the intro page first
        self.show_frame(IntroPage)

        # Shows the current frame, passed in as a parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


    def show_score_page_with_result(self, quiz_answers):
        # Here, want to do similar logic to game outcome template, but want to calculate overall score
        # Will need to check each answer and compare to the correct answer
        # Take in a dictionary, quiz_answers

        # Use "" if key cannot be found in dictionary
        # Get answers of quiz
        capital_city = quiz_answers.get("capital_city", "").strip().lower()
        winter_answer = quiz_answers.get("winter_cold","")
        lizard_species = quiz_answers.get("lizard_species","").strip().lower()

        # Check the answers and calculate the score 
        score = 0
        if capital_city == "madrid":
            score +=1
        if winter_answer == 1: # 1 = cold, 2 = not cold
            score += 1
        if lizard_species == "reptile":
            score +=1
        
        print(score)

        # Retrieve the final page frame (which shows the game result)
        win_lose_page = self.frames[ScorePage]

        # Call method on the final page, ScorePage, frame
        win_lose_page.display_result(score)
        # Show the output page 
        self.show_frame(ScorePage)



        

# Make a class for each page
class IntroPage(tk.Frame):
    # Button and title to start the game
    # Set up the class
    # ## NEW ## Add theme_bg parameter
    def __init__(self, parent, controller, theme_bg= 'SystemButtonFace'): 
        super().__init__(parent, bg=theme_bg)

        # Title label 
        title_label = ttk.Label(self, text = "Welcome to the <Name> Quiz Game!", font=("Helvetica, 14"), foreground="#32a4a8")
        # Make one box
        title_label.pack(pady=20)

        # Start button 
        start_button = ttk.Button(self, text = "Start Quiz", command = lambda: controller.show_frame(MainPage))
        start_button.pack(pady=20)

class MainPage(tk.Frame):
    # ## NEW ## Add theme_bg parameter
    def __init__(self, parent, controller, theme_bg= 'SystemButtonFace'):
        # super() lets MainPage belong to any Tkinter widget
        super().__init__(parent, bg=theme_bg)
        # Make controller to pass data from selections
        self.controller = controller

        # Configure grid for the quiz questions
        # Make a grid with one column 
        # Rows will be made by making widgets (will be placed one after the other vertically)
        # Use columnconfigure to centre rows within the column (use 1 everywhere)
        # Makes each row stretch to take up any extra space in the column
        self.columnconfigure(0, weight=1)

        current_row = 0

        # 1. Input Entry (What is the capital of Spain?)
        spain_capital_label = ttk.Label(self, text = "What is the capital of Spain?")
        spain_capital_label.grid(row=current_row, column = 0, pady=20)
        current_row += 1

        self.capital_input_var = tk.StringVar(value="")
        capital_entry = ttk.Entry(self, textvariable=self.capital_input_var)
        # To demonstrate if you want to use password type input
        #capital_entry = ttk.Entry(self, textvariable=self.capital_input_var, show="●")
        capital_entry.grid(row=current_row,column=0)
        current_row += 1

        # 2. Multiple choice (Is it normally cold in winter?)
        winter_cold_label = ttk.Label(self, text="Is it normally cold in winter?")
        winter_cold_label.grid(row=current_row, column=0, pady=20)
        current_row += 1

        self.winter_yes_no_option_state = tk.IntVar(value="")
        winter_yes_option = ttk.Radiobutton(self,text="Yes",value = 1, variable=self.winter_yes_no_option_state)
        winter_yes_option.grid(row=current_row,column=0)
        current_row += 1

        winter_no_option = ttk.Radiobutton(self,text="No",value = 2, variable=self.winter_yes_no_option_state)
        winter_no_option.grid(row=current_row,column=0)
        current_row += 1

        # 3. Another Input Entry (What species is a lizard?)
        species_label = ttk.Label(self, text="What species is a lizard?")
        species_label.grid(row=current_row, column=0, pady=20)
        current_row += 1

        self.species_var = tk.StringVar(value = "")
        species_entry = ttk.Entry(self,textvariable=self.species_var)
        species_entry.grid(row=current_row, column=0, pady=10)
        current_row += 1


        # Next button
        # The submit_choice function will call WinLosePage and pass in the data from the MainPage question
        next_button = ttk.Button(self, text = "Next", command = self.submit_choice_and_show_result)
        next_button.grid(row=current_row, column=0)



    def submit_choice_and_show_result(self):
        # Send collected responses for the questions
        quiz_responses = {
            "capital_city": self.capital_input_var.get(),
            "winter_cold": self.winter_yes_no_option_state.get(),
            "lizard_species": self.species_var.get()
        }
        # Pass the selected value to the gameApp controller
        self.controller.show_score_page_with_result(quiz_responses)
    
    def reset_fields(self):
        # Reset the input fields and multiple choice selections stored, so can be reassigned next time 
        self.capital_input_var.set("")
        self.winter_yes_no_option_state.set("")
        self.species_var.set("")

class ScorePage(tk.Frame):
    # ## NEW ## Add theme_bg parameter
    def __init__(self, parent, controller, theme_bg= 'SystemButtonFace'):
        # Write this whenever making new page 
        super().__init__(parent, bg = theme_bg)
        self.controller = controller
        # Label for result
        self.result_title_label = ttk.Label(self, text = 'Score:')
        self.result_title_label.pack(pady=(50,15))
        # Label for the score result
        self.result_message_label = ttk.Label(self, text="[Result]")
        self.result_message_label.pack(pady=(0,20))
        # Button to go back to Intro page
        back_to_intro = ttk.Button(self, text = "Start Again", command = lambda: controller.show_frame(IntroPage))
        back_to_intro.pack(pady=20)
    
    def display_result(self, result_text):
        # Set the message on the WinLosePage which shows the result (if the user has won or lost),
        # using the passed in text 
        self.result_message_label.config(text=result_text)


       
# Run the app 
app = gameApp()
app.mainloop()