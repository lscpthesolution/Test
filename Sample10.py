##################################Make FUNCTIONS##########################
def sayHello(name : str) -> str:
    return "Hello, " + name

def printYourName(name: str) -> None:
    print("Good Morning, " + name)

def makeList(first:int, second:float, third:str, forth:bool, fifth) -> list :
    result = list()
    result.append(first)
    result.append(second)
    result.append(third)
    result.append(forth)
    result.append(fifth)

    return result


########################RUN#########################
print(sayHello("Adam"))
printYourName("SE")
print(makeList(1, 3.0, "Adam", True, "This is our new chapter"))