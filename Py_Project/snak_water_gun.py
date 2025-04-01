#Here we will incorporate our learning to create a simple project of snake water gun.

print("WELCOME")
print("Snake Water Game")
print("Rules: ")
import random
play = "yes"
wins, losses, ties = 0, 0, 0
while play == "yes":
    
    print('''Choose any one :
      Snake
      Water
      Gun''')
    ch = input("Enter your choice in word :").capitalize()
    bot = random.choice(["Snake","Water","Gun"])
    print("*******************\n")
    if ch == "Snake":
        if bot == "Water":
            print("Bot chose: ", bot)
            print("Yes you won !!:) ")
            wins += 1 

        elif bot == "Gun":
            print("Bot chose: ", bot)
            print("Oh no you Lose :( ")
            losses += 1 
        elif bot == "Snake":
            print("Bot chose: ", bot)
            print("You Tied .... ")
            ties += 1
        else: 
            print("Choose only from the options given")
    if ch == "Water":
        if bot == "Gun":
            print("Bot chose: ", bot)
            print("Yes you won !!:) ")
            wins += 1
        elif bot == "Snake":
            print("Bot chose: ", bot)
            print("Oh no you Lose :( ")
            losses += 1
        elif bot == "Water":
            print("Bot chose: ", bot)
            print("You Tied .... ")
            ties += 1
        else: 
            print("Choose only from the options given")
    if ch == "Gun":
        if bot == "Snake":
            print("Bot chose: ", bot)
            print("Yes you won !!:) ")
            wins += 1
        elif bot == "Water":
            print("Bot chose: ", bot)
            print("Oh no you Lose :( ")
            losses += 1
        elif bot == "Gun":
            print("Bot chose: ", bot)
            print("You Tied .... ")
            ties += 1
        else: 
            print("Choose only from the options given")
    print(f"Score: {wins} Wins, {losses} Losses, {ties} Ties")
    play =input("Do you wish to play again against the mighty bot ?! (yes or no)")
    if play == "no":
        print("Thank you , come again when you feel lucky ;)")
    