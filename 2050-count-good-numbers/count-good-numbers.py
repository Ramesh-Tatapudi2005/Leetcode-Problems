import math
class Solution:
    def power(self,base, exp):
        if exp == 0:
            return 1
        half = self.power(base,exp // 2)
        if exp % 2 == 0:
            return (half * half) % (10**9 + 7)
        else:
            return (half * half * base) % (10**9 + 7)
        
    def countGoodNumbers(self, n: int) -> int:
        if n ==1:
            return 5
        MOD = 10 ** 9 + 7
        even = (n+1) // 2
        odd = n // 2
        ans = self.power(5,even) * self.power(4,odd) % MOD
        return ans 