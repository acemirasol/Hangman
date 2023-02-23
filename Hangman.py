import random
from words_hangman import words_list

def get_word():
    word = random.choice(words_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let us play the game Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    print("*****************************************************")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Used letter", guess)
                print("*****************************************************")

            elif guess not in word:
                print(guess, "Not in the word")
                print("*****************************************************")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job!", guess, "is in the word")
                print("*****************************************************")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indeces = [i for i, letter in enumerate(word) if letter == guess]
                for index in indeces:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Already guessed the word",guess)
                print("*****************************************************")
            elif guess != word:
                print(guess, "is not the word")
                print("*****************************************************")
                tries -= 1
                guessed_words.append(guess)
            else: 
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
            print("*****************************************************")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("The word is " +word+ ".")
        print("Wow! You guessed the word, you are amazing " )
        

        
    else:
        print("Sorry, you lose")





def display_hangman(tries):
    stages = [  """
                    --------
                    |      |
                    |      o
                    |    \\|/
                    |      |
                    |     /\\
                    -
                """,
                """
                    --------
                    |      |
                    |      o
                    |    \\|/
                    |      |
                    |     /
                    -
                """,
                """
                    --------
                    |      |
                    |      o
                    |    \\|/
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      o
                    |     \\|
                    |      |
                    |     
                    -
                """,
                """                    
                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |     
                    -
                """,
                """
                    --------
                    |      |
                    |      o
                    |    
                    |      
                    |     
                    -
                """,
                """
                    --------    
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N): ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()