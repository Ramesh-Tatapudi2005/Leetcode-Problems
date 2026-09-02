import math
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        if n ==1:
            return 5
        odd = even = math.ceil(n / 2)
        if n % 2 == 1:
            odd -= 1
        MOD = 10 ** 9 + 7
        ans = (pow(5, even, MOD) * pow(4,odd, MOD))% MOD 
        return ans 