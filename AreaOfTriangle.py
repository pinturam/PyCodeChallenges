# taking input three sides of triangle
a = float(input("enter first side of triangle :"))
b = float(input("enter second side of triangle :"))
c = float(input("enter third side of triangle :"))

# calculate of semi perimeter
s = (a+b+c)/2

# calculate area of triangle
area = (s*(s-a)*(s-b)*(s-c))**0.5

# print area
print("area of triangle is :", area)
