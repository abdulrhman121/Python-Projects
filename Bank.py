import random
import time
import string

Bank_Data = {
    4454: {"Name": "Abdulrhman", "password": 1458, "Money": 105584},
    4455: {"Name": "Ahmed", "password": 7420, "Money": 543},
}

config = {
    "Min_Deposit": 1,  # Minimum deposit amount
    "Min_Withdrawal": 1,  # Minimum withdrawal amount
    "Min_transfer": 1,  # Minimum withdrawal amount
    "Id_Num": 4,  # Number of digits in the ID
    "pass_Num": 4,  # number of password characters
    "id_chars": string.digits,  # '0123456789'
    "Prefix": "[ ! ]",  # displayed before the text.
    "Prefix_input": "[ - ]",  # It is displayed before input
}


def loading(text="wait", dots=3, sec=1):
    for i in range(1, dots + 1):
        print(f"\r{config['Prefix']} {text}{'.' * i}", end="")
        time.sleep(sec)
    print()


def create_id():
    while True:
        id = ""
        for i in range(config["Id_Num"]):
            id += random.choice(config["id_chars"])
        if int(id) not in Bank_Data and id[0] != "0" and id[1] != id[3]:
            return int(id)


def add_account():
    while True:
        Name = input(f"{config["Prefix_input"]} What is your name? ")
        if Name.strip() == "":
            print(
                f"\n{config["Prefix"]} You can't leave the name empty. You're not a ghost!\n"
            )
            continue
        else:
            break
    while True:
        password = input(f"{config['Prefix_input']} What is your password? ")
        if password.strip() == "":
            print(f"\n{config['Prefix']} Password can't be empty!\n")
            continue
        elif len(password) != config["pass_Num"]:
            print(
                f"\n{config['Prefix']} Your password must be {config['pass_Num']} digits\n"
            )
            continue
        while True:
            password2 = input(f"{config["Prefix_input"]} Write your password again: ")

            if password2 != password:
                print(f"\n{config["Prefix"]} worng! , try again..\n")
            else:
                break
        id = create_id()
        print(f"\n{config["Prefix"]} we working to create the account!")
        loading()
        print(
            f"\n{config["Prefix"]} Your name: {Name}\n{config["Prefix"]} Your id is: "
            + str(id)
        )
        Bank_Data[id] = {"Name": Name.title(), "password": int(password), "Money": 0.00}
        break


def deposit(login_id):
    while True:
        try:
            deposit_in = float(
                input(
                    f"{config["Prefix_input"]} Write down the amount you wish to deposit: "
                )
            )
            if deposit_in < config["Min_Deposit"]:
                print(f"\n{config['Prefix']} The minimum deposit amount is: {config['Min_Deposit']}")
                continue
            Bank_Data[int(login_id)]["Money"] += deposit_in
            print(f"\n{config['Prefix']} {deposit_in}$ has been added to your account!")
            break
        except ValueError:
            print(f"\n{config['Prefix']} Just numbers!")


def withdraw(login_id):
    while True:
        try:
            withdrawal_out = float(
                input(
                    f"{config["Prefix_input"]} Write down the amount you wish to withdrawal: "
                )
            )
            if withdrawal_out > Bank_Data[int(login_id)]["Money"]:
                print(f"\n{config['Prefix']} Not enough balance!")
                continue
            elif withdrawal_out < config["Min_Withdrawal"]:
                print(f"\n{config['Prefix']} The minimum withdrawal amount is: {config['Min_Withdrawal']}")
                continue
            Bank_Data[int(login_id)]["Money"] -= withdrawal_out
            print(
                f"\n{config['Prefix']} {withdrawal_out}$ has been withdrawn from your account!"
            )
            break
        except ValueError:
            print(f"\n{config['Prefix']} Just numbers!")

def transfer(login_id):
    while True:
        transfer_to = int(input("What is the identifier to which the data should be transferred? "))
        if transfer_to == login_id:
            print("You can't transfer to yourself!")
            continue
        if transfer_to not in Bank_Data:
            print("\nThis Id not found..")
            continue
        transfer_amount = float(input("How much do you wish to transfer? "))
        if transfer_amount < 1 or transfer_amount < config["Min_transfer"]:
            print(f"The minimum transfer amount is {config['Min_transfer']}")
            continue
        elif transfer_amount > Bank_Data[login_id]["Money"]:
            print("You don't have that amount of money.")
            return
        else:
            break
    while True:
        yn = input("Are you sure (y/n)? ")
        if yn.strip().lower() == "n":
            return
        elif yn.strip().lower() == "y":
            Bank_Data[login_id]["Money"] -= transfer_amount
            Bank_Data[transfer_to]["Money"] += transfer_amount
            print(f"\n{transfer_amount} were successfully transferred to {Bank_Data[transfer_to]["Name"]}, id = {transfer_to}")
            return


def check_account(login_id):
    print("\n")
    print("=" * 20)
    print(f"{config['Prefix']} Name: {Bank_Data[int(login_id)]["Name"]}")
    print(f"{config['Prefix']} Money: {Bank_Data[int(login_id)]["Money"]}$")
    print("=" * 20)
    print("\n")

def directing(login_id):
    choice = input(f"        {config["Prefix_input"]}: ")
    if choice.strip() == "1":
        deposit(login_id)
    elif choice.strip() == "2":
        withdraw(login_id)
    elif choice.strip() == "3":
        transfer(login_id)
    elif choice.strip() == "4":
        check_account(login_id)
    elif choice.strip() == "5":
        exit()
    else:
        print(f"{config['Prefix']} Invalid choice!")


def login():
    login_id = input(f"{config['Prefix_input']} What your id: ")
    login_pass = input(f"{config['Prefix_input']} What your password: ")
    if login_id.strip() == "" or login_pass.strip() == "":
        print(f"{config['Prefix']} You left id or password empty!")
        return
    try:
        login_id = int(login_id)
        login_pass = int(login_pass)
    except ValueError:
        print(f"\n{config['Prefix']} ID and password must be numbers!\n")
        return
    if login_id in Bank_Data and Bank_Data[login_id]["password"] == login_pass:
        loading(sec=1)
        print(f"{config["Prefix"]} Registration successful!")
        while True:
            print("""\nType a number: 
        [ 1 ] deposit
        [ 2 ] withdraw
        [ 3 ] transfer
        [ 4 ] check_account
        [ 5 ] exit""")
            directing(login_id)
    else:
        loading(sec=1)
        print(f"\n{config['Prefix']} Wrong id or password!\n")


def main():
    while True:
        print(f"""
{config["Prefix"]} Welcome to the Bank!
    
    [ 1 ] Create Account
    [ 2 ] Login
    [ 0 ] Exit
""")
        choice = input(f"{config['Prefix_input']} Choose: ")

        if choice.strip() == "1":
            add_account()
        elif choice.strip() == "2": 
            login()
        elif choice.strip() == "0":
            print(f"{config['Prefix']} Goodbye!")
            exit()
        else:
            print(f"{config['Prefix']} Invalid choice!")



main()
