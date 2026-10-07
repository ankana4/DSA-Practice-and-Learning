'''
You just saw all your answer scripts after correction at school but haven't received a report card yet. 
So, you want to find out the percentage that you scored. Assume the total marks for each subject to be 80.
'''
n = int(input())
total_marks = 0
for _ in range(n):
    marks = int(input("Enter marks: "))
    total_marks += marks
maximum_marks = n*80
percentage = (total_marks / maximum_marks)*100
print(f"Percentage is {percentage:.2f}")    
    