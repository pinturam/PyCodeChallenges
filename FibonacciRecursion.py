def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


terms = int(input('enter terms: '))

if terms <= 0:
    print('please enter a positive integer')
else:
    print('fibonacci series: ')
    for i in range(terms):
        print(fibonacci(i))
