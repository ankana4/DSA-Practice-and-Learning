#Given a number, find out if it is divisible by 6 or not.
t = int(input())
for _ in range(t):
    n = int(input())
    if n%6 == 0:
        print("True")
    else:
        print("False")    