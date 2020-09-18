# program to remove punctuation form a string
# define punctuation
punctuation = '''!()-[];:'"\,<>./?@#$%^&*_~'''
# take input as string from user
string = input('enter a string :')
# remove punctuation form string
no_punctuation = " "
for char in string:
    if char not in punctuation:
        no_punctuation = no_punctuation + char


# display the unpunctual string
print(no_punctuation)

