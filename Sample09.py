# freeSpace = list()
# for each in range(5):
#     freeSpace.append(input("Enter a key : "))

# print(freeSpace)



# prices = list()
# for each in range(5):
#     prices.append(input("Enter each price : "))

# print(prices)


freeSpace = ['banana', 'apple', 'kiwi', 'orange', 'water mellon']
prices = ['70', '80', '90', '100', '110']


result = dict(zip(freeSpace, prices))
print(result.keys())
print(result.values())

print(set(freeSpace))           # list -> set
print(tuple(prices))            # list -> tuple