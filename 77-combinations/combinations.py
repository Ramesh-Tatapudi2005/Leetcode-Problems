class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def combinations(ind , comb):
            if len(comb) == k:
                result.append(comb.copy())
                return 
            if ind > n:
                return 
            for i in range(ind, n+1):
                comb.append(i)
                combinations(i+1, comb)
                comb.pop()
        combinations(1, [])
        return result