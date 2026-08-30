class Solution:
    # def pown(self, num):
        
    def myPow(self, x: float, n: int) -> float:
        exp = n
        if exp < 0:
            x = 1 / x
            exp = -exp
        ans = 1
        while exp > 0:
            if exp % 2 == 1:
                ans = ans * x
                exp = exp - 1
            else:
                x = x * x
                exp = exp // 2
        return ans