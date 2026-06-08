import string
import random

# ================================= Part 1


config = {
    "min_length": 8,
    "max_length": 64,
    "chars": string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    + string.digits  # '0123456789'
    + string.punctuation,  # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
}


def generate_password(length):  # generate password
    passw = ""
    for i in range(length):
        passw += random.choice(config["chars"])
    return passw


def get_user_input():  # get user input (Create Password)
    while True:
        try:

            length = int(
                input(
                    f"How many letters do you want (Min {config["min_length"]} - Max {config["max_length"]})? "
                )
            )
        except ValueError:
            print("[!] Are you crazy? Its Just Accept Integer Number!")
        else:
            if config["min_length"] <= length <= config["max_length"]:
                return length
            else:
                print(
                    f"[!] Enter a number between {config['min_length']} and {config['max_length']}"
                )


def cmain():  # Main ( create Password)
    print(f"""Welcome To Password Creator!""")
    length = get_user_input()
    passw = generate_password(length)
    print(passw)


# ================================= Part 2


def add_inputs():  # Take web and password
    web = input("What The Website Name (ex: Google.com ) ? ")  # Google.com
    web_pass = input("What The Password  (ex:me@123!Assd ) ? ")  # me@123!Assd
    if is_duplicate(web, web_pass):
        print("[!] Already exists!")
    else:
        saver(web, web_pass)


def search_inputs():  # search for web password
    web = input("What The Website Name (ex: Google.com)? ")
    with open("Passwords.txt", "r") as f:
        for line in f:
            if web.lower() in line.lower():
                parts = line.strip().split(" : ")
                if len(parts) == 2:
                    print(f"Website  : {parts[0]}")
                    print(f"Password : {parts[1]}")
                    return
    print("Not found.")


def show_inputs():  # show web password
    try:
        with open("Passwords.txt", "r") as f:
            for line in f:
                parts = line.strip().split(" : ")
                if len(parts) == 2:
                    print(f"Website  : {parts[0]}")
                    print(f"Password : {parts[1]}")
                    print("---")
    except FileNotFoundError:
        print("[!] No passwords saved yet.")


def delete_inputs():
    web = input("What The Website Name (ex: Google.com)? ")
    try:
        with open("Passwords.txt", "r") as f:
            lines = f.readlines()

        new_lines = [line for line in lines if web.lower() not in line.lower()]

        if len(new_lines) == len(lines):
            print("[!] Not found.")
            return

        with open("Passwords.txt", "w") as f:
            f.writelines(new_lines)

        print(f"Deleted. ({web})")
    except FileNotFoundError:
        print("[!] No passwords saved yet.")


def U_Inputs():  # Taking and verifying user input
    valid = ["Add", "Search", "Show", "Delete", "Create", "Exit"]
    while True:
        U_input = input(": ")
        if U_input.strip().lower() == "exit":
            print("Goodbye.")
            exit()
        if U_input.strip().title() in valid:
            return U_input
        print("[X] Enter a valid Type.\n")


def if_else(
    U_input,
):  # Redirect the user to the appropriate function if the input is correct.
    if U_input.strip().title() == "Add":
        add_inputs()
    elif U_input.strip().title() == "Search":
        search_inputs()
    elif U_input.strip().title() == "Show":
        show_inputs()
    elif U_input.strip().title() == "Delete":
        delete_inputs()
    elif U_input.strip().title() == "Create":
        cmain()
    elif U_input.strip().title() == "Exit":
        exit()


def saver(web, web_pass):  # Save web and password in file
    with open("Passwords.txt", "a") as passsave:
        passsave.write(web + " : " + web_pass + "\n")
    print(f"Done saved. ({web})")


def is_duplicate(
    web, web_pass
):  # Check that the website ((and)) password are not duplicates.
    try:
        with open("Passwords.txt", "r") as f:
            for line in f:
                parts = line.strip().split(" : ")
                if len(parts) == 2:
                    if parts[0] == web and parts[1] == web_pass:
                        return True
    except FileNotFoundError:
        pass
    return False


def main():  # Main function
    while True:
        print("""
𝓦𝓮𝓵𝓬𝓸𝓶𝓮 To Password Manegar
    [-] To Add Password Type: Add
    [-] To Show Passwords Type: Show
    [-] To Delete Password Type: Delete
    [-] To Create Password Type: Create
    [-] To Search For Password Type: Search
    [-] To Exit Type: Exit
""")
        U_input = U_Inputs()
        if_else(U_input)


main()  # Just to run the main function
