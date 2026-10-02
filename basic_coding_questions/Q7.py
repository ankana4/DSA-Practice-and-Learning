'''
Your mother has sent you to the milkman with a cylindrical bottle. You have to pay the milkman the price for the bottle full of milk at a rate of ₹40 per litre of milk. You are given the radius (r) and the height (h) of the bottle in centimetres. 
You can assume the value of π as 3.14.
Formula for volume of cylinder:

V=π r2h

Also, 1 litre = 1000 cm3.
'''
p = 3.14
radius, height = map(int, input().split())
volumn_of_cylinder = p*radius*radius*height
liters = volumn_of_cylinder/1000
price = liters * 40
print(price)
