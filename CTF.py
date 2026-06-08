import time
import os

celsius = int(input("[!] What the temperature celsius ?"))
Fahrenheit = (celsius * 9/5) + 32
print("[!] Wait a little while..")
time.sleep(2)    # Pause 2 seconds
Result = f"[!] Your celsius temperature is : {celsius}\nYour temperature in Fahrenheit is : {Fahrenheit}"
print(Result)
if celsius <= 0 :
    print("[-]WTF how you still alive its very cold")
elif celsius < 55:
    print("[-]I love this Atmosphere its nice with my ex in one bed but she left :/")
else:
    print("[-] Are you iron man ? are you living in hell!!?")
os.system("pause")


    