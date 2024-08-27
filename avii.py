import random;
real1 = random.randint(1,100)
def easy(real,guess):
    lives = 10
    previous = []
    while (real != guess):
        previous.append(guess)
        if (guess == previous):
            print("You have guessed it already. Try something else")
        else:
            if (real > guess ):
                print("Too Low")
                lives -= 1
                print(f"Lives : {lives}")
            elif (real < guess):
                print("Too High")
                lives -= 1
                print(f"Lives : {lives}")
        if lives == 0:
            print(f"Game Over.\nYou couldn't guess the no.\nNo. was {real}")
        guess = int(input("Enter your guess : "))
    else:
        print(f"Correct guess \nNo. was {real}")

def hard(real,guess):
    lives = 5
    while (real != guess):
        if (real > guess ):
            print("Too Low")
            lives -= 1
            print(f"Lives : {lives}")
        elif (real < guess):
            print("Too High")
            lives -= 1
            print(f"Lives : {lives}")
        if (lives == 0):
            print(f"Game Over\nYou couldn't guess the no.\nThe no. was {real}")
            break
        guess = int(input("Enter your guess : "))
    else:
        print(f"Correct guess \nNo. was {real}")

level = input("Enter the difficult level 'easy' or 'hard': ").lower()
while True:
    if level == "easy":
        print("Lives: 10")
        guess1 = int(input("Enter your guess : "))
        easy(real1,guess1)
        break
    elif level == "hard":
        print("Lives: 5")
        guess1 = int(input("Enter your guess : "))
        hard(real1,guess1)
        break
    else:
        print("Please write the valid syntax")
        level = input("Enter the difficult level 'easy' or 'hard': ").lower()
