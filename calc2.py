print("------ Clac By Echo ------")


num1 = float(input("[!] First Number: "))
num2 = float(input("[!] Second Number: "))


print(f"\n-------\n [-]Your First Number is : {num1},\n [-]Your Second Number is : {num2}\n-------")


print(f"""
[-] Choose the process
[-] + : {num1} + {num2}
[-] - : {num1} - {num2}
[-] X : {num1} X {num2}
[-] / : {num1} ÷ {num2}
[-] % : {num1} % {num2}
[-] 6 : Exit
""")


pr = input("[!] Type A process: ")
re = f"Result is : {num1} {pr} {num2} = "


if pr == "+":
    print(f"{re}"+ str(num1 + num2))
elif pr == "-":
    print(f"{re}" + str(num1 - num2))
elif pr.upper() == "X":
    print(f"{re}" + str(num1 * num2))
elif pr.upper() == "/":
    if num2 == 0:
        print("It cannot be divided by zero.")
    else:
        print(f"{re}" + str(num1 / num2))
elif pr.upper() == "%":
    print(f"{re}" + str(num1 % num2))
else:
    exit()

