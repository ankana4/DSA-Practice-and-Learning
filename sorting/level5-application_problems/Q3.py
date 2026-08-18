#Sort tuples by second value
#Use Selection Sort to sort employees by salary.
employees = [("Amit", 45000), ("Riya", 62000),
("Karan", 38000), ("Meera", 55000)]
n = len(employees)
for i in range(0, n-1):
    min_index=i
    for j in range(i+1, n):
        if employees[j][1] < employees[min_index][1]:
            min_index=j
    employees[i], employees[min_index] = employees[min_index], employees[i]
print(employees)    