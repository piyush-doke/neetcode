class MyQueue:

    def __init__(self):
        self.s = list()

    def push(self, x: int) -> None:
        self.s.append(x)
        for i in range(len(self.s) -1, 0, -1):
            self.s[i], self.s[i - 1] = self.s[i - 1], self.s[i]

    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()