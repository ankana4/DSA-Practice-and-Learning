'''
Your teacher has assigned you the task of finding out the average weight of your class. 
She gives you the weights of all the students in the class and expects you to calculate the average weight of the class. 
Assume that there are only 10 students in your class.

'''
numbers = map(float, input().replace(",", "").split())
total_weight = sum(numbers)
avg_weight = total_weight / 10
print(f"{avg_weight:6f}")