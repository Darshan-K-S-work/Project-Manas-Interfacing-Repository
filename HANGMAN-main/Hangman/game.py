try:
    from playsound import playsound
except:
    pass
from time import sleep
from mymodule import totScore, misc, animals, entertainment, food, hpics, intro_scr, desc, lost_scr, win_scr, play_again, get_word, runtime_disp, guess_input, high, get_high


def theme():  # Choosing theme of words
    global words, hint, guessWord

    t = int(input(
        "\nChoose a theme(1/2/3/4):\n\t1. Animals\t2. Entertainment\t3. Food \t4. Miscellaneous\n"))
    if (t == 1):
        words = list(animals.keys())
        guessWord = get_word(words)
        hint = animals[guessWord]
    elif (t == 2):
        words = list(entertainment.keys())
        guessWord = get_word(words)
        hint = entertainment[guessWord]
    elif (t == 3):
        words = list(food.keys())
        guessWord = get_word(words)
        hint = food[guessWord]
    elif(t == 4):
        words = list(misc.keys())
        guessWord = get_word(words)
        hint = misc[guessWord]
    else:
        print("Choose a number between 1 to 4.")
        theme()


gameOver = False
missedLetters = ""
correctLetters = ""


if __name__ == "__main__":
    # The main game flow
    intro_scr()
    sleep(2)
    desc()
    sleep(4)
    theme()
    print("\n"+"Press Enter".center(23, '\t'))
    input()
    h = 0
    check = 3

    while True:  # Main running loop

        # Asking for hint
        if (len(missedLetters) == check):
            q = int(input(
                "Do you want to trade the lives left for a clue?[0(No)/1(Yes)]: "))
            if(q == 1):
                h = 3
                print("\t"+"-"*(len(hint)+40)+"\n\t\t\t Hint:  " +
                      hint + "\n" + "\t"+"-"*(len(hint)+40) + "\n")
                check = 0
            else:
                h = 1

        # Main logic
        runtime_disp(missedLetters, correctLetters, guessWord)
        guess = guess_input(missedLetters + correctLetters)

        if guess in guessWord:  # Correct guess
            correctLetters += guess
            try:
                playsound('./Sounds/good.wav')
            except:
                pass

            # Checking if won
            foundAll = True
            for i in range(len(guessWord)):
                if guessWord[i] not in correctLetters:
                    foundAll = False
                    break

            # Win screen
            if foundAll:
                print("\n"+"\t"*3+"Correct! The word is \'"+guessWord+"\'!")
                win_scr()
                totScore[0] += 1
                print("\n"+"You have a Total of: " +
                      str(totScore[0]) + "- Wins and " + str(totScore[1]) + "- Losses"+"\n")

                gameOver = True

        else:  # Wrong guess

            # Updating missed letters
            missedLetters += guess
            try:
                playsound('./Sounds/bad.wav')
            except:
                pass

            # Check if out of lives and lost screen
            if (len(missedLetters) + h) == (len(hpics)-1):  # Hint modification by h
                runtime_disp(missedLetters, correctLetters, guessWord)
                print("\nYou have run out of guesses! \nAfter "+str(len(missedLetters))+" wrong guesses and " +
                      str(len(correctLetters))+" correct guesses, the word was \'"+guessWord+"\'.\n\t\tCongrats you kinda killed a person.")
                lost_scr()
                totScore[1] += 1
                print("\n"+"You have a Total of: " +
                      str(totScore[0]) + "-Wins and " + str(totScore[1]) + "-Losses"+"\n")
                gameOver = True

        # Play again
        if gameOver:
            high()
            # Show high score
            print("All time High Score:", end=" ")
            f = open("./Files/high_score.txt", "r")
            hi = str(f.read())
            f.close()
            print(hi + " Wins\n")
            if play_again():  # Stays in while loop with reset parameters
                gameOver = False
                missedLetters = ""
                correctLetters = ""
                h = 0
                check = 3
                theme()
                print('Press Any Key'.center(23, '\t'))
                input()

            else:
                break
