import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Times New Roman"
WORK_MIN = .5 #25
SHORT_BREAK_MIN = 0.15 #5
LONG_BREAK_MIN = 0.70 #20
reps = 0
timer = None

window = tkinter.Tk()
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    time_label.config(text = "Timer")
    canvas.itemconfig(timer_text, text= "00:00")
    tick_label.config(text = "")
    global  reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_douwn(long_break_sec)
        time_label.config(text = "Long Break of 20 mins")
    elif reps % 2 == 0:
        count_douwn(short_break_sec)
        time_label.config(text = "Short break of 5 Mins")
    else:
        count_douwn(work_sec)
        time_label.config(text="Work for 25 Mins")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_douwn(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60

    canvas.itemconfig(timer_text, text =f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000,count_douwn, count-1 ) #this timer variable is assigned for reset function
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(reps/2)):
            mark += "✔"
        tick_label.config(text = mark )
# ---------------------------- UI SETUP ------------------------------- #



window.title("Pomodoro App")
window.config(padx=100, pady = 50, bg =YELLOW)

canvas = tkinter.Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image( 100, 112, image = tomato_img)
timer_text = canvas.create_text(103,130, text="00:00",fill = "white", font =(FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)



time_label = tkinter.Label(text = "Timer", font = (FONT_NAME, 35, "bold"), bg = YELLOW, fg = GREEN)
time_label.grid(column = 1, row = 0)

start_button = tkinter.Button(text = "START", command = start_timer)
start_button.grid(column = 0, row =2 )

stop_button = tkinter.Button(text = "RESET", command = reset_timer)
stop_button.grid(row= 2, column=2)


tick_label = tkinter.Label( bg = YELLOW, fg = GREEN, font =(10))
tick_label.grid(column =1 , row = 3)





window.mainloop()