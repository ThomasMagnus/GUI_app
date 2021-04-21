import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
WORK_SEC = 60
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
mark = ''

checks = [True, True, True]

window = Tk()
window.title('Timer')
window.config(padx=100, pady=100, bg=YELLOW)


def start():
    global WORK_MIN
    WORK_MIN = 25
    global WORK_SEC
    WORK_SEC = 60
    timer_txt.config(text='Work', fg=GREEN)
    canvas.itemconfig(canv_txt, text=f'{WORK_MIN}:{WORK_SEC}')
    timer()


def timer():
    global WORK_SEC
    global WORK_MIN
    if WORK_MIN > 0 or WORK_SEC > 0:
        window.after(1000, timer)
        timer_txt.config(text='Work', fg=GREEN)
        WORK_SEC -= 1
        if WORK_SEC < 0:
            WORK_SEC = 59
            WORK_MIN -= 1
        if WORK_SEC < 10 and WORK_MIN < 10:
            canvas.itemconfig(canv_txt, text=f'0{WORK_MIN}:0{WORK_SEC}')
        elif WORK_SEC < 10:
            canvas.itemconfig(canv_txt, text=f'{WORK_MIN}:0{WORK_SEC}')
        elif WORK_MIN < 10:
            canvas.itemconfig(canv_txt, text=f'0{WORK_MIN}:{WORK_SEC}')
        else:
            canvas.itemconfig(canv_txt, text=f'{WORK_MIN}:{WORK_SEC}')
        if WORK_MIN <= 5:
            timer_txt.config(text='Break', fg=PINK)
        if WORK_MIN < 1:
            window.attributes('-topmost', True)
    else:
        global mark
        mark += '✔'
        lbl = Label(text=mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, 'normal'), pady=10)
        lbl.grid(column=1, row=3)


timer_txt = Label(text='Timer', font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
timer_txt.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
canv_txt = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

start_btn = Button(text='Start', bg='white', font=(FONT_NAME, 10), padx=10, command=timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text='Reset', bg='white', font=(FONT_NAME, 10), padx=10, command=start)
reset_btn.grid(column=3, row=2)

window.mainloop()
