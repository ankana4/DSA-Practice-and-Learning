'''
Given a number, find out the sum of squares of all its digits.

If the number is represented as d1d2d3, then the sum will be d12 + d22 + d32
'''
t = int(input())
for _ in range(t):
    sum = 0
    n = input()
    for i in n:
        sum += int(i)**2
    print(sum)    