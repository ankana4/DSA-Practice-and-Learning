'''
You want to print the follow pattern.

*

**

***

****
'''
t = int(input())
for i in range(0, t+1):
    for j in range(1, i+1):
        print("*", end="")
    print()    