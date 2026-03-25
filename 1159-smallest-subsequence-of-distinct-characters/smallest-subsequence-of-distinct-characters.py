from collections import Counter
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d = Counter(s)
        visited = set()
        stack = []
        for ch in s:
            d[ch] -= 1

            if ch in visited:
                continue
            while stack and ch < stack[-1] and d[stack[-1]] >0:
                visited.remove(stack.pop())
            stack.append(ch)
            visited.add(ch)
        return "".join(stack)