# This is for inline comments
'''
This is for multi-line comments
sdjfklsjdkfl
sdjfkljsdlkf
sdjfklsdjf
'''


'''
type

* int --> 7, 8, 4
* double (float) --> 7.01, 8.88
* string (str) --> "This is my love"                        'This is my love'
* char -->         'a', 'b'                                 "a", "b"
                C, C++, Java, JavaScript, Python              Python, JavaScript
* boolean (bool) --> True/False 
    * we can make conditional statements

    if (type(4) == int):
        print(True)
    else:
        print(False)
'''



# print(3 + 5)
# print(int("3") + 5)

# you can get a value/data from the user through the terminal
# the program can be more dynamic 
# name = input("Please enter your name  : ")
# print(name)
# print(type(name))










# guess = int(input("Please enter any number between 1 and 100 : "))

# if(guess > 10):
#     print("This is bigger than 10")
# elif (guess == 10):
#     print("This is equal to 10")
# else: #guess < 10
#     print("This is less than 10")




# for variableName in Series:
#   do your work
'''
Series
    * List 
        -> list()
        -> []
        ->  l = list()       []
            l.append(7)      [7]
            l.append(8)      [7, 8]
            l.append(1)      [7, 8, 1]
                             0  1  2

            l[0]        --> 7
            l[1]        --> 8

    * Tuple

    * range(start, end, inc)

    * Dictionary

'''




'''
for and while


for variableName in Series:
    do your work
'''

l = [1,2,3,4,5,6,7,8,9]
# use the index
print("USE THE INDEX")
for each in range(0, 9, 1):
    print(l[each])


# use the value
print("USE THE VALUE")
for each in l:
    print(each)


