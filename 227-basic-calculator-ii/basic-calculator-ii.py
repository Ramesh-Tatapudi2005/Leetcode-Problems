import re
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        pro = "+"
        tokens = re.findall(r'\d+|[+\-*/]',s)
        for i in tokens:
            if i.isdigit():
                if pro == "+":
                    stack.append(int(i))
                elif pro == "-":
                    stack.append(-int(i))
                elif pro == "*":
                    stack[-1] = stack[-1] * int(i)
                elif pro == "/":
                    stack[-1] = int(stack[-1] /  int(i))
            else:
                pro = i
        return sum(stack)