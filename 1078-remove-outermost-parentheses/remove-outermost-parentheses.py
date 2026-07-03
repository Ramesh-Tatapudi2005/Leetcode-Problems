class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        level = 0
        result = ""
        for i in s:
            if i == '(':
                if level >0:
                    result += i
                level += 1
            elif i == ')':
                level -= 1
                if level > 0:
                    result += i
        return result