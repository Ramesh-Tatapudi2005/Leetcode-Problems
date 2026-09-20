class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        n = len(s)
        def generateall(curr_part, ind):
            if ind == n:
                result.append(curr_part.copy())
                return
            for i in range(ind, n):
                if ispalindrome(s, ind, i):
                    curr_part.append(s[ind: i + 1])
                    generateall(curr_part, i+1)
                    curr_part.pop()

        def ispalindrome(st, start, end):
            while start <= end:
                if st[start] != st[end]:
                    return False
                start += 1
                end -= 1
            return True
        generateall([],0)
        return result 