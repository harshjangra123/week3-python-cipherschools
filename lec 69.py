import random
winning_number = random.randint(1,100)
guess = 1

game_over = False
while True:
    number = int(input("Guess a number b/w 1 and 100- "))
    if number == winning_number:
        print(f"You win ,and you guessed this number in {guess} times ")
        break
    else:
        if number < winning_number:
            print("too low")   
        else:
            print("too high")
        guess += 1
        continue
        # DRY - don't repeat yourself 