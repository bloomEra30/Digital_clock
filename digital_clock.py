#we are using Tkinter to design our clock window
import tkinter as tk

#used to get real time system time
from datetime import datetime

#base screen where the clock will appear
screen = tk.Tk()

#will display clock title at the top
screen.title('DIGITAL CLOCK')

#window background
screen.configure(background = "navy")

#window width & height
screen.geometry('500x200')


#this function will summon and update the present time
def get_time():

    #time on 1st line & date on 2nd line
    present_time = datetime.now().strftime('%I:%M:%S %p\n%d-%m-%Y')

    #restore old time with new time on screen
    clock.config(text = present_time)

    #auto update every second. 1 second or 1000milliseconds
    clock.after(1000, get_time)

#label widget
clock = tk.Label(
    screen,
    text = "Loading...",
    font = ('Comic Sans MS', 50, "bold"),
    background = "navy",
    foreground = "Yellow"

)

#the label stays in the center
clock.pack(expand = True)


#calls the function once to start the clock
get_time()

#keeps the window open and responsive
screen.mainloop()




