print("------ Clac By Echo ------")


num1 = float(input("[!] First Number: "))
num2 = float(input("[!] Second Number: "))


print(f"\n-------\n [-]Your First Number is : {num1},\n[-]Your Second Number is : {num2}\n-------")


print(f"""
[-] Choose the process
[-] 1 : {num1} + {num2}
[-] 2 : {num1} - {num2}
[-] 3 : {num1} X {num2}
[-] 4 : {num1} ÷ {num2}
[-] 5 : Exit
""")


pr = int(input("[!] Type A Number 1 - 5: "))
prR = ""

if pr == 1:
    prR = "+"
elif pr == 2:
    prR = "-"
elif pr == 3:
    prR = "X"
elif pr == 4:
    prR = "÷"
else:
    exit()


Ru = f"[-] The Result is: {num1} {prR} {num2} = "

if pr == 1:
    print(f"{Ru}" + str(num1 + num2))
elif pr == 2:
    print(f"{Ru}" + str(num1 - num2))
elif pr == 3:
    print(f"{Ru}" + str(num1 * num2))
elif pr == 4:
    if num2 == 0:
        print("[-] It cannot be divided by zero.")
    else:
        print(f"{Ru}" + str(num1 / num2))


