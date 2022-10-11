import random


while True:
    topRange = input("Type a number: ")
    if topRange.isdigit():
        topRange = int(topRange)

        if topRange <= 0:
            print("Please type a number larger than zero next time!")
            quit()

    else:
        print("Please type a number!")
        quit()

    theNumber = random.randint(1, topRange)
    guessses = 0

    while True:
        guessses += 1
        userGuess = input("Make a guess: ")

        if userGuess.isdigit():
            userGuess = int(userGuess)
        else:
            print("Please type a number")
            continue

        if userGuess == theNumber:
            print("You guessed it!")
            break

        elif userGuess > theNumber:
                print("Guess lower")
        else:
                print("Guess higher")

    print("You got it in", guessses, "guesses!")


    playAgain = input("Do you want to play again? [Yes/No]: ")
    if playAgain == "Yes" or playAgain == "yes" or playAgain == "YES":
        continue

    else:
        print("Thanks for playing!")
        break


