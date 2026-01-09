print("-----------------------------------------------------------------------------------------------------------")
print("Welcome to the animal quiz! There are 4 questions in total! You will recieve a score at the end! Good Luck!")
print("-----------------------------------------------------------------------------------------------------------")

#USER DETAILS
while True:
    name = input("What is your first name? Please note, a name must be entered. ").strip().title()

    if not name.isalpha():
        print("--------------------------------------------------------")
        print("Name must contain letters only. No numbers or special characters.")
    elif len(name) > 20:
        print("--------------------------------------------------------")
        print("Name must be 20 characters or fewer.")
    else:
        print("--------------------------------------------------------")
        print(f"Welcome, good luck {name}!")
        break


# QUIZ DATA
import random 

questions = (
    "How many inches can a rat's teeth grow per year?: ",
    "How many strands of hair does a Chinchilla have per follicle?: ",
    "What is the average life span of a Great Dane?: ",
    "Where can you find lemurs?: ",
)

options = (
    ("1. Two inches", "2. Five inches", "3. Seven inches", "4. Ten inches"),
    ("1. One to five hairs", "2. Ten to 30 hairs", "3. 50 to 80 hairs", "4. 100 to 150 hairs"),
    ("1. Five years", "2. Ten years", "3. 15 years", "4. 20 years"),
    ("1. Madagascar and Comoros Islands", "2. Countries in Africa and Gibraltar", "3. Galapagos Islands", "4. Australia and New Zealand"),
)

answers = ("2", "3", "1", "1")

G_messages = [
            "Correct, well done!",
            "Correct, amazing",
            "Correct, excellent work",
            "Correct, great job",
            "Correct, well done clevercloggs",
            "Correct, nice one",
            ]

B_messages = [
              "Incorrect, better luck next time",
              "Incorrect, try again later",
              "Incorrect, nice try though",
              ]

# MAIN GAME LOOP
play_again = "yes"

while play_again.lower() == "yes":

    guesses = []
    score = 0
    question_number = 0

    for question in questions:
        print("--------------------------------------------------------")
        print(question)

        for option in options[question_number]:
            print(option)

        
        while True:
            guess = input("Please enter (1, 2, 3, 4): ").strip()

            if guess == "":
                 print("--------------------------------------------------------")
                 print("Whoops! You can't skip this question. Have a guess and choose 1, 2, 3, or 4.")
                 continue
            if not guess.isdigit() or len(guess) != 1:
                 print("--------------------------------------------------------")
                 print("Invalid input. You can only enter numbers. Please choose between: 1, 2, 3, or 4.")
                 continue
            if guess not in ("1", "2", "3", "4"):
                 print("--------------------------------------------------------")
                 print("Sorry! There are only four options to choose from. Please select: 1, 2, 3, or 4.")
                 continue
            break

        guesses.append(guess)

        if guess == answers[question_number]:
            score += 1
            print("--------------------------------------------------------")
            print(random.choice(G_messages))
        else:
            print("--------------------------------------------------------")
            print(random.choice(B_messages))
            print(f"The correct answer was: {answers[question_number]}")

        question_number += 1


# RESULTS

    print("--------------------------------------------------------")
    print("                        RESULTS                         ")
    print("--------------------------------------------------------")

    print("The correct answers were:", *answers)
    print("Your guesses were:", *guesses)

    score = int(score / len(questions) * 100)
    print(f"Your score is {score}%")

    play_again = input("Would you like to try again? (yes/no): ").strip().lower()

print("--------------------------------------------------------")
print(f"Thanks for playing! {name}💃🕺")
print("--------------------------------------------------------")

input("\nPress Enter to exit...")