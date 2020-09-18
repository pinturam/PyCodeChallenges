def lcm(x, y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm1 = greater
            break
        greater += 1
    return lcm1


num1 = int(input('enter first number: '))
num2 = int(input('enter second number: '))

print('LCM = ', lcm(num1, num2))
