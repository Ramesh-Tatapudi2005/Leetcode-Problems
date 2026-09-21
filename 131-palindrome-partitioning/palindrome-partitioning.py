class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        n = len(s)
        def generatepart(ind, curr_part):
            if ind == n:
                result.append(curr_part.copy())
                return 
            
            for i in range(ind, n):
                if ispalindrome(s, ind, i):
                    curr_part.append(s[ind: i +1])
                    generatepart(i+1, curr_part)
                    curr_part.pop()
            
        def ispalindrome(s, start,end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        generatepart(0, [])
        return result 