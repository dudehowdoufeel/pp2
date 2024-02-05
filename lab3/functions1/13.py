import random
def rand():
    print("Hello! What is your name?")
    name=input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    num=random.randint(1,20)
    sum=0
    while True:
        print("Take a guess.")
        n=int(input())
        sum+=1
        if(n>num):
            print("Your guess is too high.")
        elif(n<num):
            print("Your guess is too low.")
        else:
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break

rand()