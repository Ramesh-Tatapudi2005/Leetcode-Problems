class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        if n == 0 or n > 45:
            return []
        result = []
        def findcomb(ind , curr_comb, depth, n):
            if depth == 0:
                if sum(curr_comb) == n:
                    result.append(curr_comb.copy())
                return 
            for i in range(ind,10):
                if i > n:
                    break
                curr_comb.append(i)
                findcomb(i+1, curr_comb, depth-1, n)
                curr_comb.pop()
        findcomb(1, [], k,n)
        return result