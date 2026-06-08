import string
import random

config = {
    "min_length": 8, 
    "max_length": 64,
    "chars":
    string.ascii_letters # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    + string.digits # '0123456789'
    + string.punctuation # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
}

def generate_password(length):
    passw = ""
    for i in range(length):
        passw += random.choice(config["chars"])
    return passw

def get_user_input():
    while True:
        try:
            
            length = int(input(f"How many letters do you want (Min {config["min_length"]} - Max {config["max_length"]})? "))
        except ValueError:
            print("[!] Are you crazy? Its Just Accept Integer Number!")
        else:
            if config["min_length"] <= length <= config["max_length"]:
                return length
            else:
                print(f"[!] Enter a number between {config['min_length']} and {config['max_length']}")


def main():
    while True:
        print(f"""Welcome To Password Creator!""")
        length = get_user_input()
        passw = generate_password(length)
        print(passw)
        again = input("Wanna start again? (y/n) ")
        if again.strip().lower() == "n":
            exit()


main()