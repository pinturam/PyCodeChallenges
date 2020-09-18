num = int(input('enter a number: '))

if num < 0:
    print('enter a positive number')
else:
    s = 0
    while num > 0:
        s += num
        num -=1
    print(s)
