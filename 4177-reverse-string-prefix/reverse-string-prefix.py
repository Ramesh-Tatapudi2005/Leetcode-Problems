class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if k == 1 or len(s) < k:
            return s
        l, r = 0, k -1
        s = list(s)
        while l <= r:
            s[l], s[r] = s[r] , s[l]
            l += 1
            r -= 1
        return "".join(s)