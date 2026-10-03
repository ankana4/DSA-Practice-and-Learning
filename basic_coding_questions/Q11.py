#Given a two-digit number n, print both the digits of the number.

t = int(input())
for _ in range(t):
    n = int(input())
    first_digit = n // 10
    second_digit = n % 10
    print(first_digit, second_digit)    