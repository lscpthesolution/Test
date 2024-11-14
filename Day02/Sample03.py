class Person:  
    def __init__(self, name: str, age : int) -> None:
        self.name = name
        self.old = age


p01 = Person("Adam", 19)
print(p01.name)
print(p01.old)

