class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0,1
        if n == 0:
            return 0
        if n == 1:
            return 1
        for i in range(1,n):
            f2= f1 + f0
            f0,f1 = f1,f2
        return f1