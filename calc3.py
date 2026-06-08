# calculator By A.Ulrhman
# Functions 

# Functions 1

def GetNumbers(): 
    while True:
        try:
            num1 = float(input("Your First Number: "))
            num2 = float(input("Your Second Number: "))
            return num1, num2
        except ValueError:
            print("[X] Enter a valid number!\n")

# Functions 2

def ShowMenu(num1,num2): 
    print(f"""
    Choose the process:
    [+] {num1} + {num2}
    [-] {num1} - {num2}
    [x] {num1} x {num2}
    [/] {num1} ÷ {num2}
    [%] {num1} % {num2}
    Type "Exit" to exit
        """)

# Functions 3   

def GetParameter(): 
    valid = ["+", "-", "x", "X", "/", "%"]  
    while True:
        para = input("Type A Parameter: ")
        if para.lower() == "exit":
            print("Goodbye!")
            exit()
        if para in valid:
            return para
        print("[X] Enter a valid process!\n")

# Functions 4

def calculate(num1,num2,para): 
# para = Parameter 

    Result = f"[-] {num1} {para} {num2} = " # A consistent result message for shortening codes instead of writing them multiple times

# ---- Calculate Functions

    if para == "+":
        print(Result + str(num1 + num2))

    elif para == "-":
        print(Result + str(num1 - num2))

    elif para.upper() == "X":
        print(Result + str(num1 * num2))

    elif para == "/":
        if num2 == 0:
            print("It Cannot Be Divided By Zero.")
        else:
            print(Result + str(num1 / num2))

    elif para == "%":
        print(Result + str(num1 % num2))



# Main Function
def main():
        print("------ Clac By A.Ulrhman ------")
        while True:

            num1, num2 = GetNumbers()

            ShowMenu(num1,num2)
            
            para = GetParameter()

            calculate(num1,num2,para)

            again = input("Start Again? (y/n) ")
            if again.lower() == "n":
                print("Goodbye!")
                break
            
# To Run Main Functhion

if __name__ == "__main__":
    main()

# End of the source 