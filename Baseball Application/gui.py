# At this point, the GUI is still in development and non-functional.

import tkinter as tk
import baseball

def start_game():
    team1 = team1_input.get()
    team2 = team2_input.get()
    baseball.main()

    

# Initializing the main window

root = tk.Tk()
root.geometry("600x400")
root.title("Scorchsoft Baseball Scoring")



# Team 1 Label
team1_label = tk.Label(root, text="Team 1", font=('Arial', 14))
team1_label.pack(pady=10)

# Team 1 Input
team1_input = tk.Entry(root, font=('Arial', 14))
team1_input.pack(pady=10)

# Team 2 Label
team2_label = tk.Label(root, text="Team 2", font=('Arial', 14))
team2_label.pack(pady=10)

# Team 2 Input
team2_input = tk.Entry(root, font=('Arial', 14))
team2_input.pack(pady=10)

# Creating the button frame 

buttonframe = tk.Frame(root)
buttonframe.pack(pady=20)

# Start Game Button inside the buttonframe
start_button = tk.Button(buttonframe, text="Start Game", font=('Arial', 14))
start_button.grid(row=0, column=0, sticky=tk.W+tk.E)
# Run the main loop
root.mainloop()