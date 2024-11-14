target = 25

# for each in range(target, -1, -1):
#     try:
#         print(target/each)
#     except:
#         print("Error")


################ check if it is a triangle ###############
def findBiggest(t):
    biggest = -9999
    for each in t:
        if biggest < each:
            biggest = each

    return biggest

def checker(target):
    #show your work here
    for eachT in target:
        print(eachT)
        big = findBiggest(eachT)
        twoSum = 0
        # for regular T
        for each in eachT:
            if  big != each:
                twoSum = twoSum + each
        # for E T
        if twoSum == 0:
            for each in range(0, 2, 1):
                twoSum = twoSum + eachT[each]
                
        if twoSum > big:
            print(True)
        else :
            print(False)

        
        
########################RUN########################
triangle = [(3,3,3),(4,5,2),(1,2,5)]
checker(triangle)

triangle = [(7,3,4),(4,1,2),(3,2,7)]
checker(triangle)
# 