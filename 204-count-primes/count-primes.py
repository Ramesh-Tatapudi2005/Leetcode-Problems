import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n > 2:
            is_prime = [1] * (n)
            is_prime[0] = is_prime[1] = 0
            for i in range(2,int(math.sqrt(n))+1):
                if is_prime[i]:
                    for j in range(i*i,n, i):
                            is_prime[j] = 0
        else:
            return 0
        return is_prime.count(True)
