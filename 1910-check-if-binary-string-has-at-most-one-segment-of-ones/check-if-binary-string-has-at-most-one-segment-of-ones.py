class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        c = False
        if len(s) == 1:
            return True
        for i in range(1,len(s)):
            if s[i] == '0':
                c = True
            else:
                if c:
                    return False
        return True