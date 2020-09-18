x = input("enter value of x :")
y = input("enter value of y: ")

# create a temporary variable and swap the values
temp = x
x = y
x = y
y = temp

print("after swapping x is {}".format(x))
print("after swapping y is {}".format(y))
