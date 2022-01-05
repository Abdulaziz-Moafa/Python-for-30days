secret_word = "azoz"

guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
number_of_guess = 0

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        print(3 - guess_count, "attempt left")
        guess = input("enter the guess ")
        guess_count += 1


    else:
        out_of_guesses = True

if out_of_guesses:
    print("you lose ")
else:
    print("you win")

