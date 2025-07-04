from tkinter import *
import speedtest

def speed_test():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6),3)) + " Mbps"
    upload = str(round(sp.upload()/(10**6),3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=upload)

sp = Tk()
sp.title(" Internet Speed test   ")
sp.geometry("500x650")
sp.config(bg="blue")


lab = Label(sp, text="Internet Speed test", font=("Times new roman", 30, "bold"), bg="blue", fg="white")
lab.place(x=60, y=40, height=50, width=380)

lab = Label(sp, text="Download Speed", font=("Times new roman", 30, "bold"))
lab.place(x=60, y=130, height=50, width=380)

lab_down = Label(sp, text="00", font=("Times new roman", 30, "bold"))
lab_down.place(x=60, y=200, height=50, width=380)

lab = Label(sp, text="Upload Speed", font=("Times new roman", 30, "bold"))
lab.place(x=60, y=290, height=50, width=380)

lab_up = Label(sp, text="00", font=("Times new roman", 30, "bold"))
lab_up.place(x=60, y=360, height=50, width=380)

Button = Button(sp, text="Check Speed", font=("Time new roman", 30, "bold"), relief=RAISED, bg="green", command=speed_test)
Button.place(x=60, y=460, height=50, width=380)


sp.mainloop()
