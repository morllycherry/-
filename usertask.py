#---coding:utf-8---

import time
import os
import tkinter
from verificationpart import*

top = tkinter.Tk(className="")
verification1
def sum_t():
    print("Welcome")
time.sleep(1)
print("Please type the server address")
one = True
while one:
    time_start = time.time()
    first = str(input("Address:"))
    if first == '000.000.000.000':
        print("Confirmed domain name")
        one = False
        time_end = time.time()
        sum_t = (time_end - time_start)
        print("time cost",sum_t,"s")

        two = True
        while two:
            time_start = time.time()
            second = str(input("what is your at"))
            third = str(input("Please input a password:"))
            if second == 'inside.user':
                if third == '0':
                    print("thats right")
                    two = False
                    time_end = time.time()
                    sum_t = (time_end - time_start)
                    print("time cost",sum_t,"s")
                    time.sleep(5)

                    three = True
                    while three:
                        time_start = time.time()
                        print("Please select the option you need")
                        print("Please choose 1 for logout and 2 for shutdown")
                        fourth = str(input("choice:"))
                        if fourth == '1':
                            print("Successfully logged out")
                            three = False
                            time_end = time.time()
                            sum_t = (time_end - time_start)
                            print("time cost",sum_t,"s")
                        elif fourth == '2':
                            print("executing...")
                            time.sleep(2)
                            os.system("shutdown -s -t 60")
                            print("Your computer will shut down in a minute")
                            STOP = str(input("To cancel, enter stop:"))
                            if STOP == 'stop':
                                os.system("shutdown /a")
                                print("shutdown has been canceled")
                            else:
                                print("Invalid instruction")
                        else:
                            print("Under development")

            elif second == 'inside.user':
                if third != '0':
                    print("Account or password error, please try again")

            else:
                print("Account or password error, please try again")

    else:
        print("This address is not valid")

top.mainloop()
