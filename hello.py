import time
from time import sleep
from tqdm import tqdm
import os
from os import system

print("Version 1.12")
time.sleep(1)
print("reloading...")
print("The security component starts loading...")

max = 100
 
for i in tqdm(range(max)):
    sleep(0.1)
print("The security component started successfully")
ac = input(str(("Please enter your account number:")))
pd = input(str("Please enter your password:"))

if ac == "2022153177":
    if pd == "350036177":
        print("Confirmed!")
        print("Waiting to join server selection...")
        time.sleep(4)

    else:
        print("Warning: account error")
        print("Perform clear restart...")
        max = 100
 
        for i in tqdm(range(max)):
            sleep(0.01)
        print("Warning: you are about to sign out of your login")
        time.sleep(2)
        os.system("shutdown -s -t  60 ")
        exe = "Warning: fatal error" 
        while exe :
            print(exe)

elif ac == "839255636":
    if pd == "HAOhao123":
        print("Confirmed!")
        print("Waiting to join server selection...")
        time.sleep(4)

    else:
        print("Warning: account error")
        print("Perform clear restart...")
        max = 100
 
        for i in tqdm(range(max)):
            sleep(0.01)
        print("Warning: you are about to sign out of your login")
        time.sleep(2)
        os.system("shutdown -s -t  60 ")
        exe = "Warning: fatal error" 
        while exe :
            print(exe)
        


else:
    print("Warning: account error")
    print("Perform clear restart...")
    max = 100
 
    for i in tqdm(range(max)):
        sleep(0.01)

    print("Warning: you are about to sign out of your login")
    time.sleep(2)
    os.system("shutdown -s -t  60 ")
    exe = "Warning: fatal error" 
    while exe :
        print(exe)


