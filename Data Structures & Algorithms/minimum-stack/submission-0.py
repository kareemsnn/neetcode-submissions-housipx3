class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        print(self.stack)
        if val < self.minimum:
            self.minimum = val

    def pop(self) -> None:
        self.stack.pop()
        print(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
