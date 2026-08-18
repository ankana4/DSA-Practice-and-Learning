#Sort dictionaries by marks
#Use Insertion Sort to sort in descending order of marks.
students = [{"name":"A", "marks":76}, {"name":"B", "marks":91},
{"name":"C", "marks":68}, {"name":"D", "marks":84}]

n = len(students)
for i in range(1, n):
    key = students[i]
    j = i-1
    while j>=0 and students[j]["marks"] < key["marks"]:
        students[j+1] = students[j]
        j -= 1
    students[j+1] = key
print(students)        