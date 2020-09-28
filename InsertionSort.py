# Insertion Sort:
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i -1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
            lst[j+1] = key


# main
lst1 = []
n = int(input('Enter size of list: '))
print('Enter elements of list: ')
for i in range(0, n):
    e = int(input())
    lst1.append(e)


insertion_sort(lst1)
print('Sorted list is: ')
for i in range(len(lst1)):
    print(lst1[i])
