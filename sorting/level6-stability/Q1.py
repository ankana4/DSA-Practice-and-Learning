#Demonstrate stability
#Sort by marks. A stable algorithm should preserve A before C and B before D.
[("A",80), ("B",70), ("C",80), ("D",70)]

students = [("A", 80), ("B", 70), ("C", 80), ("D", 70)]
for i in range(1, len(students)):
    key = students[i]
    j = i-1
    while j>0 and students[j][1] > key[1]:
        students[j+1] = key
        j -= 1
    students[j+1] = key
print(students)    
    