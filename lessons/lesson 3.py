class Bank:
    def __init__(self, name, pin, money):
        self.name = name
        self._pin = pin
        self.__money = money
    def __str__(self):
        return f'{self.name} : {self.__money}'
    def setpin(self, pin):
        self._pin = pin
    def getpin(self):
        print(self._pin)
beka = Bank('beka', '2525', 10_000)
print(beka)
beka.setpin(4343)
beka.getpin()

print(beka)
print(dir(beka))

