# program to print all prime numbers between an interval

# take input from user
lower = int(input('enter lower range: '))
upper = int(input('enter upper range: '))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)