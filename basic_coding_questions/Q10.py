'''
Given a number, find out if it is odd or even.

There are multiple tests in this.
'''
n = int(input())
for i in range(n):
    t = int(input())
    if t%2==0:
        print("EVEN")
    else:
        print("ODD")    