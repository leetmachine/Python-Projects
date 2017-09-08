import random

#game loop and logic
def game():
    # generate a random number between 1 and 10
    secret_num = random.randint(1, 10)

    tries = 5
    # get a number guess from the player
    while tries != 0:
            try:
                guess = int(input("Guess a number between 1 and 10: "))

            except ValueError:
                print("{} is not a number".format(guess))
            # compare the guess to the secret number
            if guess == secret_num:
                print("You got it! My number was {}".format(secret_num))
                break;
            elif guess > secret_num:
                print("Your guess is too high. Try again!")

            elif guess < secret_num:
                print("Your guess is too low. Try again!") 

            tries-= 1

    else:
        print("You lose! My number was {}".format(secret_num))

    return

#game start and end prompt
while True:
    cont = input("Would you like to play? Type YES or NO: ")

    if cont == 'YES':
        game()

    else:
        print("Bye.")
        break



