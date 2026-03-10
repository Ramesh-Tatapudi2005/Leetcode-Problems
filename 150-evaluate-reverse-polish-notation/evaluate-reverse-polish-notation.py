class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        top = -1
        f = s = 0
        if len(tokens) == 1:
            return int(tokens[0])
        for i in tokens:
            if i == '+' and top != 0 and top != -1:
                f = int(stack.pop())
                s = int(stack.pop())
                stack.append(s+f)
                top -= 1
                # print(i,stack[top],stack)
            elif i == '-' and top != 0 and top != -1:
                f = int(stack.pop())
                s = int(stack.pop())
                stack.append(s-f)
                top -= 1
                # print(i,stack[top],stack)
            elif i == '*' and top != 0 and top != -1:
                f = int(stack.pop())
                s = int(stack.pop())
                stack.append(s*f)
                top -= 1
                # print(i,stack[top],stack)
            elif i == '/' and top != 0 and top != -1:
                f =int(stack.pop())
                s = int(stack.pop())
                stack.append(int(s/f))
                top -= 1
                # print(i,stack[top],stack)
            else:
                stack.append(i)
                top += 1
                # print(stack)
        return stack[top]