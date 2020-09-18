num = int(input('enter a number: '))
s = 0
temp = num
while temp > 0:
    digit = temp % 10
    s += digit ** 3
    temp //= 10

if num == s:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')