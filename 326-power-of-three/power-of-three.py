class Solution:
    def recursion(self, n):
        if n == 1:
            return True
        if n <= 0 or n % 3 != 0:
            return False
        return self.recursion(n // 3)
    def isPowerOfThree(self, n: int) -> bool:
        return self.recursion(n)