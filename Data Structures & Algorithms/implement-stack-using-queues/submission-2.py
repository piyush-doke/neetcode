from collections import deque

class MyStack:

    def __init__(self):
        self.use_q1 = True
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        primary_q = self.q1 if self.use_q1 else self.q2
        primary_q.append(x)

    def pop(self) -> int:
        primary_q = self.q1 if self.use_q1 else self.q2
        secondary_q = self.q1 if not self.use_q1 else self.q2
        for i in range(len(primary_q) - 1):
            x = primary_q.popleft()
            secondary_q.append(x)
        self.use_q1 = not self.use_q1
        return primary_q.popleft()

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x

    def empty(self) -> bool:
        primary_q = self.q1 if self.use_q1 else self.q2
        return len(primary_q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()