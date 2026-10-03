#Given a set of numbers, print them in the reversed order.
t = int(input())
numbers = list(map(int, input().split()))
print(*numbers[::-1])