import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n > 2:
            is_prime = [True] * (n)
            is_prime[0] = is_prime[1] =     False
            for i in range(2,int(math.sqrt(n))+1):
                if is_prime[i]:
                    for j in range(i*i,n, i):
                        if is_prime[j]:
                            is_prime[j] = False
        else:
            return 0
        # print(is_prime)
        return is_prime.count(True)
