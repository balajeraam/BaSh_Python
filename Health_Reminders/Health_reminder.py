# importing tkinter module that will handle display window and text
import tkinter as tk

#Create a class that will generate new tkinter window with message for a given text
def Reminder(reminder_text):
    app_window = tk.Tk()
    # The bell method will adds a bell sound
    app_window.bell()
    # Text given inside the class will be converted into a label in this section
    reminder_label= tk.Label(text = reminder_text,foreground ="white",background="grey",font="bold")
    reminder_label.pack()
    # Window gets destroyed after 10000 milliseconds..what a fancy way to say 10 seconds :-). 
    app_window.after(10000,app_window.destroy)
    app_window.mainloop()

# Replace <<   >> with your name
Reminder("Hi <<   >>..Take a 30 second walk please..")
Reminder("Hi <<   >>..Drink a glass of water please..")
