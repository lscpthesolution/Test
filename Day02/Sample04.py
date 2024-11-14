class Bank:
    def __init__(self, money) -> None:
        self.__total = money            # private









123456789123123123123    # getter
    def getTotal(self) -> int:
        return self.__total
    # setter





########## RUN ##################
shinhan = Bank(100)
print(shinhan.getTotal())
# shinhan.total = 9999999999
# print(shinhan.total)