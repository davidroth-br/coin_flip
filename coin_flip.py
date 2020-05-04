from random import randint

heads_or_tails = "\n1 - Heads\n2 - Tails\nHeads or tails? "
total_count = 0
wins = 0

def flip_coin():
    return randint(1, 2)

def y_n_input(message):
    while True:
        y_n = input(message).lower()
        if y_n != "y" and y_n != "n":
            print("You must choose either 'y' or 'n'.")
            continue
        else:
            return y_n

print("Welcome to Coin Flip!\n")
play = y_n_input("Ready to play? (y/n): ")
while play == "y":
    try:
        choice = int(input(heads_or_tails))
    except:
        print("Invalid choice.")
        continue
    if choice == 1:
        print("You chose Heads.")
    elif choice == 2:
        print("You chose Tails.")
    else:
        print("Invalid choice.")
        continue

    print("Flipping the coin...")
    total_count += 1
    flip = flip_coin()
    print("Heads!") if flip == 1 else print("Tails!")
    if flip == choice:
        wins += 1
        print("You win!!!\n")
    else:
        print("You lose!!!\n")
    print("You have won {0} times in {1} tries.\n".format(wins, total_count))
    play = y_n_input("Would you like to play again? (y/n): ")
print("Goodbye!")
