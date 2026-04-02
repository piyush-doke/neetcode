class MyStack:

    def __init__(self):
        self.bucket = list()

    def push(self, x: int) -> None:
        self.bucket.append(x)

    def pop(self) -> int:
        return self.bucket.pop()

    def top(self) -> int:
        return self.bucket[-1]

    def empty(self) -> bool:
        return len(self.bucket) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()