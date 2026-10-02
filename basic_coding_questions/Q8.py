'''
You and your friend decide to play a game where given some numbers, you have to find the maximum number. 
If the maximum is an even number, you win and if it is odd, your friend wins.
'''
N = int(input("Enter a number: "))
n = list(map(int, input().split()))
max_num = max(n)
if max_num % 2 == 0:
    print("YOU WIN")
else:
    print("FRIEND WINS")    