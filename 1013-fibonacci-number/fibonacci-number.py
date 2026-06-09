class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0,1
        if n <= 1:
            return n
        for _ in range(1,n):
            f0,f1 = f1,f1+f0
        return f1