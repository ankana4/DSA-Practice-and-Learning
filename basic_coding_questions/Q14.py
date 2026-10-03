#Given a number, you have to determine if the number is greater than 7, equal to 7, or less than 7.
t = int(input())
for _ in range(t):
    n = int(input())
    if n > 7:
        print("UP")
    elif n<7:
        print("DOWN")
    else:
        print("EQUAL")
                