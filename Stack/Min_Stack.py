# https://neetcode.io/problems/minimum-stack/question


class MinStack:
    def __init__(self):
        self.stack = list()
        self.min_stack = list()

    def push(self, value: int) -> None:
        self.stack.append(value)
        # val = min(value, self.min_stack[-1] if self.min_stack else value)
        if not self.min_stack or self.min_stack[-1] > value:
            self.min_stack.append(value)
        else:
            self.min_stack.append(self.min_stack[-1])
        # self.min_stack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]