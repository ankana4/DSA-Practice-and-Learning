#Given a number n, print all the numbers that from 1 to n that are not divisible by 3.

t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(1, n+1):
        if i%3 != 0:
            print(i, end=" ") 
    print()               
            
            