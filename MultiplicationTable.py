# program to print multiplication table of a number
# ...

num = int(input('enter a number: '))

for i in range(1, 11):
    print(num, 'x', i, '=', num * i)
