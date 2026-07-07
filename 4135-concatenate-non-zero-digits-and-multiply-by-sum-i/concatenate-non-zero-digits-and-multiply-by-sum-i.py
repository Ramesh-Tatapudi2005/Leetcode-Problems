class Solution:
    def sumAndMultiply(self, n: int) -> int:
        nonzerodits = 0
        s = 0
        ans = 0
        p = 0
        while n != 0:
            rem = n % 10
            if rem != 0:
                nonzerodits = (rem * 10**p) + nonzerodits
                s += rem
                p += 1
            n = n//10
        return nonzerodits * s