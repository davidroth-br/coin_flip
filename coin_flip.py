from random import randint

heads_or_tails = "\n1 - Heads\n2 - Tails\nHeads or tails? "

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
    flip = flip_coin()
    print("Heads!") if flip == 1 else print("Tails!")
    print("You win!!!\n") if flip == choice else print("You lose!!!\n")
    play = y_n_input("Would you like to play again? (y/n): ")
print("Goodbye!")
