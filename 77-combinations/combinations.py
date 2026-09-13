class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combinations(ind , comb):
            if len(comb) == k:
                result.append(comb.copy())
                return 
            rem = k - len(comb)
            for i in range(ind, n - rem+2):
                comb.append(i)
                combinations(i+1, comb)
                comb.pop()
        combinations(1, [])
        return result