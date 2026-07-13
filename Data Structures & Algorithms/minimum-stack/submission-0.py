class MinStack:

    def __init__(self):
        # main stack to store values
        self.stack = []
        # auxiliary stack to store minimums
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # push to min_stack if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        # if popped value is the current min, remove from min_stack too
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
