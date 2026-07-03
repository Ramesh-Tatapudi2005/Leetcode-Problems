class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        s = s+s
        i , j = 0, n-1
        while j < len(s):
            print(s[i:j+1])
            if s[i:j+1] == goal:
                return True
            j += 1
            i += 1

        return False