import math
from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
background = YELLOW
counting_from = WORK_MIN
timer = None
start_or_stop = False

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(countdown_timer, text="25:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global start_or_stop
    if start_or_stop:
        start_or_stop = False
    else:
        start_or_stop = True
    countdown(counting_from * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global start_or_stop
    if start_or_stop :
        secs = f"{count % 60 :02d}"
        mins = math.floor(count / 60)
        canvas.itemconfig(countdown_timer, text=f"{mins}:{secs}")
    if count > 0 and start_or_stop:
        global timer
        timer = window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.geometry("500x500")
window.title("Pomodoro")
window.config(bg=background, padx=75, pady=70)


canvas = Canvas(width=200, height=224, bg=background, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
countdown_timer = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 27, "bold"))
canvas.grid(column=1, row=1)

button_start = Button(width=10, text="Start / Stop", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(width=10, text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)

heading = Label(text="Timer", font=(FONT_NAME, 40, "bold"), fg=GREEN, highlightthickness=0, bg=background)
heading.grid(column=1, row=0)

def listbox_click(event):
    x = listbox.get(listbox.curselection())
    global counting_from
    global WORK_MIN
    global SHORT_BREAK_MIN
    global LONG_BREAK_MIN
    if x == "Pomodoro":
        counting_from = WORK_MIN
        canvas.itemconfig(countdown_timer, text="25:00")
    if x == "Short Break":
        counting_from = SHORT_BREAK_MIN
        canvas.itemconfig(countdown_timer, text="5:00")
    if x == "Long Break":
        counting_from = LONG_BREAK_MIN
        canvas.itemconfig(countdown_timer, text="20:00")

listbox = Listbox(height=3)
types_of_timers = ["Pomodoro", "Short Break", "Long Break"]
for timer in types_of_timers:
    listbox.insert('end', timer)
listbox.grid(column=1, row=3)
listbox.config(width=15)
listbox.bind("<<ListboxSelect>>", listbox_click)


window.mainloop()

