from time import *
import random as r

def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error = error + 1 
        except:
            error = error + 1
    return error
    
def speed_time(time_s, time_e, userinput):
    time_delay = time_e - time_s
    time_r = round(time_delay,2)
    speed = len(userinput)/ time_r
    return round(speed)


if __name__ == '__main__':
    while True:
            ch = input("Ready to type(yes/no): ")
            if ch == "yes": 
                test = ["A paragraph is  a self contained unit of discourse in writing dealing with a particluar in writing dealing with a particluar point or ideal.",
                "My name is keshav", "welcome to hullikate keshav leaves here."]
                test1 = r.choice(test)
                print("  ***** Typing speed ***** ")
                print(test1)
                print()
                print()
                time_1 = time()
                testinput = input("Enter: ")
                time_2 = time()

                print('speed:', speed_time(time_1,time_2,testinput),"w/sec")
                print("Error: ", mistake(test1,testinput))
            
            elif ch == "no":
                print("Thank you")
                break

            else:
                print("Wrong input")