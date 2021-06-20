# defining strings using single quotes
string = 'Hello there'
print(string)

# defining strings using double quotes
string2 = "Double Qoute String"
print(string2)

# defining strings using tripple quotes
string3 = '''Tripple Quote String'''
print(string3)

# Multi-line strings
string4 = '''My name is Jane Doe,
    I like travelling so much'''
print(string4)

# printing the first character of the string
string = 'Hello there'
print(string[0])

# printring the  last index
print(string[-1])

#slicing 1st to 8th character
string = 'hello there'

# Print the string between index 0 to 8
print('string[1:8] = ', string[1:8])

# original text
string = 'THIS IS TEXT IN UPPERCASE'

# print transformed string
print(string.lower())

# initial string 
string = 'this text is in lowercase'

# transform to upper case
new_string = string.upper()

# print transformed string
print(new_string)

# The string
string = 'programming is fun'

# getting the length of the string
print(len(string))

# initial string
string = 'Hello?world?this?is?my?test?for?the?game'

# splitting the string
new_string = string.split("?")

# printing the new string
print(new_string)

# iterable object
object = ['Hello', 'world', 'this', 'is', 'my', 'test', 'for', 'the', 'game']

# specify the separator
separator = ' '

# Join where the comma occurs
print(separator.join(object))

# string
string = 'Hello world'

# Find the occurence of world
y = string.find('world')

print(y)

# string
string = 'Hello world, this world are a nice world'

# replace world with people
y = string.replace('world', 'people')

# print the output
print(y)

# Iterating through a string
for letter in 'Hello World':
    print(letter)

# count the number of letter
count = 0
string = 'Hello. how. is home from th lool above'
for letter in string:
    if(letter == 'o'):
        count+=1
print('The letter o occurs ' +str(count)+ ' times')   

# concatenating Strings using the plus operator
# string 1
string1 = 'section'

#string 2
string2 = 'engineering'

#concatenated string
string3 = string1 + string2

#printing the output
print(string3) 

# input string 
inputString = 'Hello World'

# string to find
stringToCheck = 'World'

# membership test
x = stringToCheck in inputString

#print output
print(x)


# Using % operator 
name = 'dianne sandra'
print('My name is %s' %name)

# using format option 
print ("{} is a good platform.".format("Section Engineering Education"))

# substitution using variable names
print ('{name} is {age} years old and she is a {occupation}'
.format(name = 'Dianne', age = 19, occupation = 'programmer'))

# emebeding variables into string constants using f-string
string1 = 'Hello'
string2 = 'world'

# print the embeded string
print(f'{string1}  {string2}')