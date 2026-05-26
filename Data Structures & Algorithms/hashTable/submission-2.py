class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
class HashTable:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = [None] * capacity
        self.size = 0

    def insert(self, key: int, value: int) -> None:
        index = self.hash(key)
        while True:
            if self.map[index] == None:
                self.map[index] = Node(key, value)
                self.size += 1
                if self.size >= self.cap//2:
                    self.resize()
                return
            elif self.map[index].key == key:
                self.map[index].val = value
                return
            index += 1
            index = index % self.cap

    def get(self, key: int) -> int:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index+=1
            index = index % self.cap
        return -1
    
    def hash(self, key:int)->int:
        return key % self.cap

    def remove(self, key: int) -> bool:
        index = self.hash(key)
        while self.map[index] != None:
            if self.map[index].key == key:
                self.map[index] = None
                self.size-=1
                return True
            index += 1
            index = index % self.cap
        return False

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        self.size = 0
        oldmap = self.map
        self.map = [None] * self.cap
        for node in oldmap:
            if node:
                self.insert(node.key, node.val)

