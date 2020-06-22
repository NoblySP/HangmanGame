print("""
Welcome to the Hangman game!

INSTRUCTIONS:
One player thinks of a word.
The other player (guessing player) tries to guess it by suggesting letters. If the player does not guess the word within 6 guesses, they lose.

The word to guess is represented by a row of dashes, representing each letter of the word.

If the guessing player suggests a letter which occurs in the word, all occurences of that letter appear in the correct positions and the number of guessess remains unchanged.
If the suggested letter does not occur in the word, one element of a hanged man stick figure is drawn and the number of guesses is increased by 1.

NOTE: You cannot guess the whole word in a single try. You have to type its letters one by one.


Game Begins! \n\n
""")


def hangman():
    total_guesses = 6    
    global guesses
    guesses = 0

    global answer
    answer = list(input("Enter a word for the other player to guess: "))
    print("")

    placeholder = list("_" * len(answer))
    print("The word is:", " ".join(placeholder), end="\n\n")
    
    global tried_letters
    tried_letters = []
    
    
    while guesses < total_guesses:
        user_guess = input("Guess a letter: ")

        
        if len(user_guess) != 1 or user_guess.isalpha() != True:
            print("Enter a valid input. Please try again! \n")
            continue

        if user_guess in tried_letters:
            print("You have already tried that letter. Please enter another letter. \n")
            continue
        

        if user_guess in answer:
            print(f"Yes, '{user_guess}' is a part of the word!")

            for ind, val in enumerate(answer):
                if user_guess == val:
                    placeholder[ind] = val
            
            print("Word:"," ".join(placeholder))
            
        else:
            print(f"'{user_guess}' is not a part of the word")
            tried_letters.append(user_guess)
            guesses += 1
            print(f"You have {total_guesses - guesses} guesses left! Try guessing again.")
            print("Incorrect Letters:", tried_letters)
            stick_figure()
            

        if placeholder == answer:
            print("\nCongrats, you WIN! You have guessed the right word! \n\n")
            play_again()
            break
    
        print("")



def stick_figure():
    if guesses == 1:
        print("""
            _______
            |     |
            O     |
                  |
                  |
                  |
                  |
                  |
                  |
            -------
            """)

    elif guesses == 2:
        print("""
            _______
            |     |
            O     |
            !     |
            !     |
                  |
                  |
                  |
                  |
            -------
            """)
        
    elif guesses == 3:
        print("""
            _______
            |     |
            O     |
            !     |
            !     |
           /      |
                  |
                  |
                  |
            -------
            """)
        
    elif guesses == 4:
        print("""
            _______
            |     |
            O     |
            !     |
            !     |
           / \    |
                  |
                  |
                  |
            -------
            """)

    elif guesses == 5:
        print("""
            _______
            |     |
            O     |
           \!     |
            !     |
           / \    |
                  |
                  |
                  |
            -------
            """)

    elif guesses == 6:
        print("""
            _______
            |     |
            O     |
           \!/    |
            !     |
           / \    |
                  |
                  |
                  |
            -------
            """)
        print("You are out of guesses")
        print("YOU LOSE!")
        print("The correct word was:", "".join(answer), end = "\n\n\n")
        play_again()


def play_again():
    again = input("Do you want to try again? [Yes/No] \n")

    if again == "Yes":
        hangman()
    else:
        print("Thank you for playing!")
    


if __name__ == "__main__":
    hangman()

