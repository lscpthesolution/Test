# class -> function -> variable
# class.variable            X
# class.function            O
# function.variable         O

class Student:
    def __init__(self, name:str, id:str) -> None:
        self.__name = name
        self.__id = id

    # getter
    '''
    return the class variable, __name
    '''
    def getName(self) -> str:
        return self.__name

    # Setter

    '''
    set a new student ID and return None
    '''
    def setID(self, givenID:str) -> None:
        self.setID = givenID


    '''
    set a new name and return None
    '''
    def setName(self, name:str) -> None:
        self.__name = name



s01 = Student("Adam", "123123")
s02 = Student("Seon", "125489")

# print(s01.__name)
# print(s02.__name)
# print(s01.__id)
# s01.__id = "11111111"
s01.setID("1111111")
print(s01.getName())
s02.setName("Now")
print(s02.getName())