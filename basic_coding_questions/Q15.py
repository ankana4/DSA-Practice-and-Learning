'''
Given three sticks with lengths L1, L2, L3 - find out if these sticks can form a triangle.

If they can form a triangle, calculate the circumference of the triangle.

Circumference of a triangle (C) = L1 + L2 + L3

The condition to be satisfied for three sticks to form a triangle is that the sum of lengths of any two sides of the triangle should be greater than or equal to the length of the third side.
'''
t = int(input())
for _ in range(t):
    l1, l2, l3 = map(int, input().split())
    if l1+l2 >= l3 and l2+l3>= l1 and l1+l3>=l2:
        circumference = l1+l2+l3
        print(circumference)
    else:
        print(-1)    