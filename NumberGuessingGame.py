from random import randint

start = 1
end = 100
value = randint(start, end)
guesses = 10
counter = 1

print("I'm thinking of a number between", start, "and", end)
print('You have', guesses, 'guesses to get it.')

guess = None

while counter<11:
    print('Guess #', counter)
    text = input("Guess the number: ")
    guess = int(text)

    if guess == value:
        print('Congrats!')
        break
    elif guess < value:
        print("Too Low.")
    elif guess > value:
        print("Too High")

    counter += 1

print("Right Answer:", value)