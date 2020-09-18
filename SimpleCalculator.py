# define functions
def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    return x / y


print('Select Operation:')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Divide')

choice = input('enter your choice : ')

num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(sub(num1, num2))
elif choice == '3':
    print(mul(num1, num2))
elif choice == '4':
    print(div(num1, num2))
else:
    print("Invalid input")