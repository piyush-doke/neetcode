class MyQueue:

    def __init__(self):
        self.s1 = list()    # inbox
        self.s2 = list()    # outbox

    def push(self, x: int) -> None:
        self.s1.append(x)
    
    def _move(self) -> None:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

    def pop(self) -> int:
        self._move()
        return self.s2.pop()

    def peek(self) -> int:
        x = self.pop()
        self.s2.append(x)
        return x

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()