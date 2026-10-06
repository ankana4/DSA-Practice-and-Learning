'''
A palindrome is a word that reads the same backward as forward, e.g., madam. 
If you start comparing the letters from the beginning with the corresponding letters from the end, they would be the same.

Given a set of words, you have to find if they are palindrome or not.
'''

t = int(input())
for _ in range(t):
    word = input()
    reversed_word = word[::-1]
    if reversed_word == word:
        print("True Palindrome")
    else:
        print("False Not Palindrome")    