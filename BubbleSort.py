# Implementing Bubble Sort

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0,len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]


# main:
lst1 = []
n = int(input('Enter size of list: '))
print('Enter elements: ')
for i in range(0, n):
    e = int(input())
    lst1.append(e)
# lst = [12,23,24,235,124]
bubble_sort(lst1)
print('Sorted list is: ')
for i in range(len(lst1)):
    print(lst1[i])
