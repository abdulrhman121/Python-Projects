import random

# main.py
# │
# ├── choices()      # تقرأ اختيار اللاعب وتتحقق منه
# ├── choices()    # تولد اختيار الكمبيوتر بـ random
# ├── determine_winner(p, c)   # تحدد الفائز وترجع النتيجة
# ├── display_result(p, c, r)  # تطبع النتيجة بشكل واضح
# └── main()                   # تربط كل شيء في loop

# Rock Paper Scissors | By A.ulrhman

# Constants


choices = ["Rock","Paper","Scissors"]
Ppoints = 0
Apoints = 0


# Functions

def choiceS():
    while True:
        pchoice = input("Choice Someting: ")
        if pchoice.title() in choices:
            aipchoice = random.choice(choices)
            return pchoice, aipchoice
        else:
            print("[X] Enter Rock, Paper, or Scissors only!\n")

def determine_winner(pchoice, aipchoice):
    global Apoints,Ppoints
    if (pchoice.title() == aipchoice):
        return("Draw!")
    
    # Player win!
    elif pchoice.title() == "Rock"     and aipchoice == "Scissors": Ppoints +=1; return "You win!" 
    elif pchoice.title() == "Scissors" and aipchoice == "Paper":    Ppoints +=1; return "You win!" 
    elif pchoice.title() == "Paper"    and aipchoice == "Rock":     Ppoints +=1; return "You win!"

    # Player lose!
    elif pchoice.title() == "Rock"     and aipchoice == "Paper":    Apoints+=1; return "You lose!"
    elif pchoice.title() == "Scissors" and aipchoice == "Rock":     Apoints+=1; return "You lose!"
    elif pchoice.title() == "Paper"    and aipchoice == "Scissors": Apoints+=1; return "You lose!"


def display_result(pchoice, aipchoice, r,Ppoints,Apoints):
    print(f"Your Choice: {pchoice} | Computer Choice: {aipchoice }\nResult: {r}\nPoints: {Ppoints} : {Apoints}")


def main():
    while True:
        print("""-- Welcome to rps game --
        Choices :
        [-]  Rock
        [-]  Paper
        [-]  Scissors""")
        pchoice, aipchoice  = choiceS()
        r = determine_winner(pchoice, aipchoice)
        display_result(pchoice, aipchoice, r,Ppoints,Apoints)
        again = input("Wanna play again (y/n)? ")
        if again.lower() == "n":
            break
        
main()
