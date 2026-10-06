#Given a number n, you have to print the multiplication table of n till the 10th multiple.

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, 11):
        mul = n*i
        print(mul, end=" ")   
    print()     