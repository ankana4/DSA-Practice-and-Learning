'''
It is the year 2020 and your father owns a restaurant. 
You have decided to spend time helping him out in the COVID-19 pandemic situation. 
You have been conducting temperature checks for all the workers and the delivery boys at the restaurant. 
A temperature above 98.6℉ is considered high and you need to flag it to your
father with a list of employees with high temperatures.
'''
t = int(input())
emp = []
for _ in range(t):
    name, temp = input().split()
    temp = float(temp)
    if  temp > 98.6:
        emp.append(name)
print(emp)    