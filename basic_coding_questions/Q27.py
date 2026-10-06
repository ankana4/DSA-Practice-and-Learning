'''
You had your birthday party last night and received a lot of candies. 
You do not want keep so many and decide to distribute it among your friends. 
To make things interesting, you plan to give each friend a number of candies equal to the number of vowels in thier first name.

You can assume that the first name of your friends consists of only one word (no spaces or special characters) and you have enough candies for each of them.

You have to determine how many candies each of your friend gets.
'''
t = int(input())
vowels = ["a", "e", "i", "o", "u"]
upper_vowels = ["A", "E", "I", "O", "U"]
for _ in range(t):
    name = input()
    count = 0
    for ch in name:
        if ch in vowels or ch in upper_vowels:
            count += 1
    print(count)        
            
            
    