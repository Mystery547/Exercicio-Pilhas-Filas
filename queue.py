class Queues:
    def __init__(self):
        self.__data = []
    
    def __str__(self):
        return str(self.__data)

    def getQueue(self):
        return self.__data

    def enterData(self, newData):
        return self.__data.append(newData)

    def remove(self):
        return self.__data.pop(0)

    def removeData(self, data):
        pos = self.__data.index(data)
        for i in range(0, pos + 1):
            self.__data.pop(0)

    def lenQueue(self):
        return len(self.__data)