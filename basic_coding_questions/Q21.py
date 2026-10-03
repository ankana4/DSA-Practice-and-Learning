#Write a program to print the letters of the word "WORKATTECH" with two letters in one line.
letter = 'WORKATTECH'
for ch in range(0, len(letter), 2):
    print(letter[ch], letter[ch+1], sep="")