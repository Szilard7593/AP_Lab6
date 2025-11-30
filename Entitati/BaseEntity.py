class BaseEntity:
    def __init__(self,id: int):
        self.__id = id

    def getID(self):
        return self.__id

    def setID(self,id):
        self.__id = id

    def __str__(self):
        return f"{self.__id}"