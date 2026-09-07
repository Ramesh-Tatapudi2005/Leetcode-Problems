class Solution:
    def climbStairs(self, n: int) -> int:
        def solve(n ,prev , curr):
            if n == 0:
                return curr
            return solve(n-1, curr, curr+ prev)
        return solve(n, 0,1)