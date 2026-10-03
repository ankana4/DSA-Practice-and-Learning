#Given a 3-digit number, you have to reverse the number.

n = int(input())
rev = 0
while n>0:
    last_digit = n%10
    rev = rev * 10 + last_digit
    n = n//10
print(rev)
