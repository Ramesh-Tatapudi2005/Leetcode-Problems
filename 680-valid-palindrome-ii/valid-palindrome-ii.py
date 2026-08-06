class Solution:
    def checkPalindrome(self,st):
        l , r = 0, len(st)-1
        while l <= r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True
    def validPalindrome(self, s: str) -> bool:
        ls = list(s)
        temp = []
        l ,r = 0, len(ls) -1
        if self.checkPalindrome(ls):
            return True
        while l <= r:
            if ls[l] != ls[r]:
                if self.checkPalindrome(ls[l:r]) and self.checkPalindrome(ls[l+1:r+1]):
                    return True
                elif self.checkPalindrome(ls[l:r]):
                    return True
                elif self.checkPalindrome(ls[l+1:r+1]):
                    return True
                else:
                    return False
            l += 1
            r -= 1
        return False