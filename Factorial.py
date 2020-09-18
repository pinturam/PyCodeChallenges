# program to find factorial of a number
num = int(input('enter a number: '))

factorial = 1
if num < 0:
    print('sorry, factorial does not exist for negative number')
elif num == 0:
    print('factorial = 1')
else:
    for i in range(1, num+1):
        factorial = factorial*i
    print('the factorial = ', factorial)