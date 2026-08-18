#Sort even and odd values separately
#Even numbers should come first in ascending order, followed by odd numbers in ascending order.
n = [7, 2, 9, 4, 1, 6]
even_index = 0
for i in range(0, len(n)):
    if n[i] % 2 == 0:
        n[i], n[even_index] = n[even_index], n[i]
        even_index += 1
 
for i in range(0, even_index-1):
    min_index = i
    for j in range(i+1, even_index):
        if n[j] < n[min_index]:
            min_index = j
    n[i], n[min_index] = n[min_index], n[i]

for i in range(even_index, len(n)-1):
    min_index = i
    for j in range(i+1, len(n)):
        if n[j] < n[min_index]:
            min_index = j
    n[i], n[min_index] = n[min_index], n[i]
print(n)                     


#Another way
odd_index = 0
for i in range(0, len(n)):
    if n[i] % 2 != 0:
        n[i], n[odd_index] = n[odd_index], n[i]
        odd_index += 1

for i in range(0, odd_index-1):
    min_index=i
    for j in range(i+1, odd_index):
        if n[j] < n[odd_index]:
            min_index = j
    n[i], n[min_index] = n[min_index], n[i] 

for i in range(odd_index, len(n)-1): 
    min_index=i
    for j in range(i+1, len(n)):
        if n[j] < n[min_index]:
            min_index = j
    n[i], n[min_index] = n[min_index], n[i]
print(n)