'''
Return a list consists of five different numbers from the user
'''
def makeFunc() -> list:
    result = list()
    for each in range(5):
        num = input("Enter any number : ")
        result.append(num)

    return result


'''
return the sum of the two given numbers
'''
def adder(first:int, second:int) -> None:
    print(first + second)

######################  RUN ###########################################3
# print(makeFunc())

adder(10, 9)