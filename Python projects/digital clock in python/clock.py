from tkinter import *
import datetime

def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    date = time.strftime('%d')
    month = time.strftime('%m')
    year = time.strftime('%y')
    day = time.strftime('%a')
    lab_hr.config(text=hr)
    lab_min.config(text=min)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date)
    lab_mon.config(text=month)
    lab_year.config(text=year)
    lab_day.config(text=day)
    lab_hr.after(200, date_time)


clock = Tk()
clock.title("         *****  digital clock  *****")
clock.geometry("1000x500")
clock.config(bg="yellow")

lab_hr = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_hr.place(x=120, y=50, height=120, width=100)
lab_hr_txt = Label(clock, text="HOUR", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_hr_txt.place(x=120, y=200, height=30, width=100)

lab_min = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_min.place(x=340, y=50, height=120, width=100)
lab_min_txt = Label(clock, text="MINs..", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_min_txt.place(x=340, y=200, height=30, width=100)

lab_sec = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_sec.place(x=560, y=50, height=120, width=100)
lab_sec_txt = Label(clock, text="SEC..", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_sec_txt.place(x=560, y=200, height=30, width=100)

lab_am = Label(clock, text="00", font=('times new roman', 40, "bold"), bg="red", fg="white")
lab_am.place(x=780, y=50, height=120, width=100)
lab_am_txt = Label(clock, text="AM/PM", font=('times new roman', 15, "bold"), bg="red", fg="white")
lab_am_txt.place(x=780, y=200, height=30, width=100)


#  ***** date ************/
lab_date = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_date.place(x=120, y=280, height=120, width=100)
lab_date_txt = Label(clock, text="DATE", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_date_txt.place(x=120, y=430, height=30, width=100)

lab_mon = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_mon.place(x=340, y=280, height=120, width=100)
lab_mon_txt = Label(clock, text="MONTH", font=('times new roman', 15, "bold"), bg="red", fg="white")
lab_mon_txt.place(x=340, y=430, height=30, width=100)

lab_year = Label(clock, text="00", font=('times new roman', 60, "bold"), bg="red", fg="white")
lab_year.place(x=560, y=280, height=120, width=100)
lab_year_txt = Label(clock, text="YEAR", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_year_txt.place(x=560, y=430, height=30, width=100)

lab_day = Label(clock, text="00", font=('times new roman', 40, "bold"), bg="red", fg="white")
lab_day.place(x=780, y=280, height=120, width=100)
lab_day_txt = Label(clock, text="DAY", font=('times new roman', 20, "bold"), bg="red", fg="white")
lab_day_txt.place(x=780, y=430, height=30, width=100)

date_time()

clock.mainloop()