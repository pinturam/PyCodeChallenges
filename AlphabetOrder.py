# program to sort words in alphabetic order

# taking a string
string = input('enter a string :')
# splitting the string into list of words
words = string.split()
# sort the list
words.sort()
# display the sorted words
for word in words:
    print(word)
