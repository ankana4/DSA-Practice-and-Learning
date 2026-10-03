'''
Given a temperature t in Centigrade, convert it into Fahrenheit.

Formula for conversion:

Temp (℉) = (9t / 5) + 32
'''
from decimal import Decimal
t = int(input())
for _ in range(t):
    n = Decimal(input())
    temp = (9*n / 5) + 32
    print(f"{temp:.2f}")
