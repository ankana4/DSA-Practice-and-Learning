'''
A binary number is a number composed of 0s and 1s.
Given a binary number, check if the number has adjacent zeroes or not, 
i.e., if two zeroes are present side by side or not.
'''
t = int(input())
for _ in range(t):
    n = input()
    found = False
    for i in range(len(n)-1):
        if n[i] == "0" and n[i+1] == "0":
            found = True
            break
    if found:
        print("Yes")
    else:
        print("No")    