#A number is known as an Armstrong number if the sum of the cubes of all its digits is equal to the number itself.
t = int(input())
for _ in range(t):
    total = 0
    n = input()
    for i in n:
        total += int(i)**3
    if total == int(n):
        print("Armstrong")
    else:
        print("Not Armstrong")    