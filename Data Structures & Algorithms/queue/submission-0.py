class Deque:
    
    def __init__(self):
        self.deque = []

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def append(self, value: int) -> None:
        self.deque.append(value)

    def appendleft(self, value: int) -> None:
        self.deque.insert(0, value)

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque.pop()

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        return self.deque.pop(0)
