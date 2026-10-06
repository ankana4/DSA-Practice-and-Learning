'''
You just made a new friend at school and he is trying to guess your birthday. 
He has already guessed the month and year of your birth, and is now trying to guess the date d.
'''
t = int(input())
while True:
    guess = int(input())
    if t == guess:
        print("Correct guess")
        break
    else:
        print("Incorrect guess")
        