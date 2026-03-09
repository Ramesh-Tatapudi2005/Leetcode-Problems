class Solution:
    def isValid(self, s: str) -> bool:
        top = -1
        stack = []
        for i in s:
            if top == -1:
                stack.append(i)
                top += 1
            elif stack[top] == '(' and i == ')':
                stack.pop()
                top -= 1
            elif stack[top] == '{' and i == '}':
                stack.pop()
                top -= 1
            elif stack[top] == '[' and i == ']':
                stack.pop()
                top -= 1
            else:
                stack.append(i)
                top += 1
        return top == -1