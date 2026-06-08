from start import *



start()
while True:
    try:
        words_count = int(input("How many words do you want to learn? "))
        break
    except ValueError:
        print("Enter a valid number")

lines = read(words_count)

correct_points = 0

for word in lines:
    while True:
        word2 = word.split()[0]
        word3 = word.split()[1:]
        answer = input(f"What : \"{word2}\" Meaning ? ")

        if normalize(answer.strip()) in [normalize(w) for w in word.split()[1:]]:
            print("Good This Is True - Keep Going!")
            correct_points +=1
            correct_file(word)
            remove_word(word)
            break
        elif answer.strip().lower() == "n":
            print(f"{word2} = {word3}")
            break
        elif answer.strip().lower() == "r":
            rest_word()
            exit()
        elif answer.strip().lower() == "q":
            exit()
        else:
            print("False - Try Again")

print(f"You Have {correct_points} word corrcet out of {words_count}\n")
