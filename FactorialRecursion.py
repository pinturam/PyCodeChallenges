def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)


num = int(input('enter a number: '))

if num <= 0:
    print('sorry, factorial does not exist for negative number')
elif num == 0:
    print('factorial = 0')
else:
    print('factorial = ', factorial(num))