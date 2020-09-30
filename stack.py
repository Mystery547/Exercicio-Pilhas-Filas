class Stack:
    def __init__(self):
        self.__data = []

    def getStack(self):
        return self.__data

    def push(self, newData):
        return self.__data.append(newData)

    def pop(self):
        return self.__data.pop()

    def showTop(self):
        return (self.__data[len(self.__data)-1])

    def emptyStack(self):
        while len(self.__data) != 0:
            self.__data.pop()