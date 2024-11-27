from itertools import count
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    label.config(text="TIMER")
    canvas.itemconfig(title_text,text="00:00")
    check_mark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    if reps%8==0:
        countdown(long_break_sec)
        label.config(text="LONG BREAK",fg=PINK)
    if reps%2==0:
        label1=Label(text="✔")
        label.grid()
        countdown(short_break_sec)
        label.config(text="SHORT BREAK", fg=RED)
    else:
        countdown(work_sec)
        label.config(text="WORK", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec<10:
        count_sec=f'0{count_sec}'
    canvas.itemconfig(title_text,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,countdown,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for i in range(work_session):
            mark+="✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro Test")
window.config(padx=100,pady=50,bg=YELLOW)
#create the canvas
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
title_text=canvas.create_text(100,112,text="00:00",fill="white",font=(FONT_NAME,25,"bold"))
canvas.grid(column=1,row=1)
label=Label(text="TIMER",font=(FONT_NAME,35,"bold"),fg=GREEN,bg=YELLOW)
label.grid(column=1,row=0)
start_button=Button(text="start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)
reset_button=Button(text="reset",highlightthickness=0,command=reset)
reset_button.grid(column=2,row=2)
check_mark=Label(text="✔",fg=GREEN,bg=YELLOW)
check_mark.grid(column=1,row=3)
window.mainloop()