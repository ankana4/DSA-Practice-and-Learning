'''
Given a number, find the sum of its digits.

If the number is represented as d1d2d3d4d5, then the sum will be d1 + d2 + d3 + d4 + d5.
'''
t = int(input())
for _ in range(t):
    sum = 0
    n = input()
    for i in n:
        sum += int(i)
    print(sum)    
        