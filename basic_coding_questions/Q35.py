'''
Given an integer matrix (2D array) of dimension m*n (m rows, n columns), 
find out the largest integer in the entire matrix.
'''
m, n = map(int, input().split())
largest = None
for i in range(m):
    row = list(map(int, input().split()))
    for j in range(n):
        if largest is None or row[j] > largest:
            largest = row[j]
print(largest)            