import random
import time

print("\nWelcome to Hangman game\n")
name = input("Please enter your name: ")

print("Hi " + name + "! Best of Luck!")
time.sleep(2)

print("Let's play Hangman!")
time.sleep(3)

def main():
    global count
    global disp
    global play
    global already_g
    global word
    global length
    
    list_of_words = ["love", "rohit", "run", "python", "water", "food", "nose", "film", "nine", "visit"
                   , "winter",  "monsoon",  "tasty"]
    word = random.choice(list_of_words)
    length = len(word)
    count = 0
    disp = '_' * length
    already_g = []
    play = ""

def playLoop():
    global play
    play = input("Do you want to play again? y = yes, n = no \n")
    while play not in ["y", "n", "Y", "N"]:
        play = input("Do you want to play again? y = yes, n = no \n")
    if play == "y":
        main()
    elif play == "n":
        print("Thanks For Playing!")
        exit()

def hangman():
    global count
    global disp
    global play
    global word
    global already_g
    
    limit = 5
    guess = input("This is the Hangman Word: " + disp + " Enter your guess: \n")
    guess = guess.strip()
    if len(guess.strip()) == 0 or len(guess.strip()) >= 2 or guess <= "9":
        print("Invalid Input, Try a letter\n")
        hangman()


    elif guess in word:
        already_g.extend([guess])
        index = word.find(guess)
        word = word[:index] + "_" + word[index + 1:]
        disp = disp[:index] + guess + disp[index + 1:]
        print(disp + "\n")

    elif guess in already_g:
        print("Please try another letter.\n")

    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||     \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  ||     | \n"
                 "  ||     |\n"
                 "  ||     | \n"
                 "  ||      \n"
                 "  ||      \n"
                 "  ||      \n"
                 "__||__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||     | \n"
                  "  ||     O \n"
                  "  ||      \n"
                  "  ||      \n"
                  "__||__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  ||     | \n"
                  "  ||     |\n"
                  "  ||     | \n"
                  "  ||     O \n"
                  "  ||    /|\ \n"
                  "  ||    / \ \n"
                  "__||__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", *already_g,  word)
            playLoop()

    if word == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        playLoop()

    elif count != limit:
        hangman()

main()
hangman()