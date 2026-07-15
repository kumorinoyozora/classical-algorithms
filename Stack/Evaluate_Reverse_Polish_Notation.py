# https://neetcode.io/problems/evaluate-reverse-polish-notation/question


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == "+":
                stack.append(stack.pop() + stack.pop())
            elif t == "-":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(v2 - v1)
            elif t == "*":
                stack.append(stack.pop() * stack.pop())
            elif t == "/":
                v1, v2 = stack.pop(), stack.pop()
                stack.append(int(v2 / v1))
            else:
                stack.append(int(t))
        return stack[-1]


tokens=["1","2","+","3","*","4","-"]
print(Solution().evalRPN(tokens))