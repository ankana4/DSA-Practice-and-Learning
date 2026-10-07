'''
In mathematics, the Fibonacci numbers (Fn) form a sequence, called the Fibonacci sequence, 
such that each number is the sum of the previous two numbers.

The first number in the sequence (F1) is 0, the second number (F2) is 1.

F1 = 0
F2 = 1
F3 = F1 + F2 = 0 + 1 => 1
F4 = F2 + F3 = 1 + 1 => 2
F5 = F3 + F4 = 1 + 2 => 3
F6 = F4 + F5 = 2 + 3 => 5
.
.
.
Fn = Fn-2 + Fn-1

Given a number (n), print the first n fibonacci numbers.
'''
t = int(input())
for _ in range(t):
    n = int(input())
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        next_sum = a+b
        a = b
        b = next_sum
    print()    