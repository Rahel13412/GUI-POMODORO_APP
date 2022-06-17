from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_time():
    global reps
    screen.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    timer_text.configure(text="Timer")
    check_mark.configure(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_text.configure(text="Break", fg="red")
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_text.configure(text="Short Break", fg="pink")
    else:
        count_down(work_sec)
        timer_text.configure(text="Work Time")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = screen.after(1000, count_down, count - 1)
    else:
        start_timer()
        print(reps)
        mark = ""
        work_session = math.floor(reps / 2)
        for i in range(work_session):
            mark += "$"
        check_mark.configure(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Pomodoro Technique")
screen.minsize(width=500, height=500)
screen.configure(bg=GREEN, padx=50, pady=100)

canvas = Canvas(width=200, height=224, bg=GREEN, highlightthickness=0)  # creating canvas
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)  # adding picture on canvas
time_text = canvas.create_text(100, 130, text="00:00", fill="black", font=(FONT_NAME, 35, "bold"))  # adding text on
# canvas
canvas.grid(row=1, column=1)

timer_text = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=GREEN, padx=5)
timer_text.grid(row=0, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 20, "bold"), command=start_timer)
start_button.grid(row=2, column=0)

restart_button = Button(text="Restart", font=(FONT_NAME, 20, "bold"), command=reset_time, )
restart_button.grid(row=2, column=2)

check_mark = Label(bg=GREEN)
check_mark.grid(row=2, column=1, )

screen.mainloop()
