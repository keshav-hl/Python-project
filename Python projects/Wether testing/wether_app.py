from tkinter import *
from tkinter import ttk
import requests

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city +"&appid=3b5556cb972e0e413f5d7f204bf4d9b3").json()
    w11_label.config(text=data["weather"][0]["main"])
    w22_label.config(text=data["weather"][0]["description"])
    w33_label.config(text=str(int(data["main"]["temp"]-273.15)))
    w44_label.config(text=data["main"]["pressure"])

win = Tk()
win.title(" **** Wether App **** ")
win.geometry("500x550")
win.config(bg="blue")

Label_tit = Label(win, text="Wether App", font=("times new roman", 35, "bold"), fg="black")
Label_tit.place(x=50, y=50, height=50, width=400)

city_name = StringVar()

list_name = indian_states = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]

com = ttk.Combobox(win, text="Wether App", values = list_name, font = ("Times new roman", 30, "bold"),textvariable=city_name)
com.place(x=50, y=120, height=50, width=400)

w1_label = Label(win, text="wether climate:", font=("Time new roman", 20, "bold"))
w1_label.place(x=50, y=280, height=40, width=200)
w11_label = Label(win, text="", font=("Time new roman", 20, "bold"))
w11_label.place(x=270, y=280, height=40, width=200)

w2_label = Label(win, text="Wether Description", font=("Time new roman", 15, "bold"))
w2_label.place(x=50, y=340, height=40, width=200)
w22_label = Label(win, text="", font=("Time new roman", 15, "bold"))
w22_label.place(x=270, y=340, height=40, width=200)

w3_label = Label(win, text="Temperature", font=("Time new roman", 20, "bold"))
w3_label.place(x=50, y=400, height=40, width=200)
w33_label = Label(win, text="", font=("Time new roman", 20, "bold"))
w33_label.place(x=270, y=400, height=40, width=200)

w4_label = Label(win, text="pressure", font=("Time new roman", 20, "bold"))
w4_label.place(x=50, y=460, height=40, width=200)
w44_label = Label(win, text="", font=("Time new roman", 20, "bold"))
w44_label.place(x=270, y=460, height=40, width=200)

down_button = Button(win, text="Done", font=("Time new roman", 20, "bold"), command=data_get)
down_button.place(x=200, y=200, height=50, width=100)

win.mainloop()
