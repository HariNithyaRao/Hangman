#							WELCOME TO HANGMAN 💀

import random
print("H A N G M A N")
def play():
        l = ['python', 'java', 'kotlin', 'javascript']
        secretword= random.choice(l)
        alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        temp = []
        for i in range(len(secretword)):
                temp.append("-")
        repeated_word = []
        mistake = 8
        while (True):
                print("".join(temp))
                guess = input("Input a letter: ")
                if len(guess) > 1 or guess == "":
                        print("You should input a single letter")
                        print("That letter doesn't appear in the word")
                elif guess not in alphabets:
                        print("Please enter a lowercase English letter")
                        print("That letter doesn't appear in the word")
                else:
                        repeated_word.append(guess)
                        if guess in secretword:
                                if repeated_word.count(guess) < 2:
                                        for m in range(len(secretword)):
                                                if secretword[m] == guess:
                                                        temp[m] = guess
                                else:
                                        print("You've already guessed this letter")
                                
                        else:
                                if repeated_word.count(guess) >= 2:
                                        print("You've already guessed this letter")
                                        print("That letter doesn't appear in the word")
                                else:
                                        mistake -= 1
                                        print("That letter doesn't appear in the word")
                if mistake == 0 :
                        print("You lost!")
                        break
                if temp.count("-") == 0:
                        print("You guessed the word" + " " + secretword + "!")
                        print("You survived!")
                        break 
                print()
wish = input('Type "play" to play the game, "exit" to quit: ')
print()
if wish == 'play':
        play()
        
