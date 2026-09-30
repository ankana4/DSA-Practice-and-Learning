#You are having a get together at your house and your mother asks you to distribute candies equally amongst all your cousins. You want to determine if the number of candies given by your mother can be equally distributed or not.

candy, cousin = map(int, input().split())
distribute = candy % cousin
if distribute == 0:
    print("YES")
else:
    print("NO")    
    