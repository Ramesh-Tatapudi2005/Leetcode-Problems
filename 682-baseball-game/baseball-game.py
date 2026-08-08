class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for ope in operations:
            if ope == '+':
                stack.append(stack[-1] + stack[-2])
            elif ope == 'D':
                stack.append(stack[-1] *2 )
            elif ope == 'C':
                stack.pop()
            else:
                stack.append(int(ope))
        return sum(stack)