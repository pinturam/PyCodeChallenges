# program to print fibonacci series
# ...

# taking terms
terms = int(input('enter terms :'))
# initialize first two terms
n1 = 0
n2 = 1
count = 2
# check if terms is valid or not
if terms <= 0:
    print('please, enter a positive interger')
elif terms == 1:
    print('Fibonacci series: ', n1)
else:
    print('Fibonacci series: ', n1, ",", n2, end=",")
    while count < terms:
        nth = n1 + n2
        print(nth, end=',')
        n1 = n2
        n2 = nth
        count += 1
