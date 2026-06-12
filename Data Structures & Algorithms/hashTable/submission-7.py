class Pair:
    def __init__(self, key, value):
        self.key = key
        self.val = value

class HashTable:
    
    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.map = [None] * self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, value)
                self.size+=1
                if 2 * self.size >= self.cap:
                    self.resize() 
                break
            if self.map[index].key == key:
                self.map[index].val = value
                break
            index += 1
            index = index % self.cap
    
    def hash(self, key:int)->int:
        return key % self.cap

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.cap
        return -1 

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -=1
                return True
            index += 1
            index = index % self.cap
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.size = 0
        self.cap *= 2
        oldmap = self.map
        self.map = [None] * self.cap
        for i in oldmap:
            if i:
                self.insert(i.key, i.val)