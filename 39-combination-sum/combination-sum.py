class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def generatecombinations(ind , current_comb, target):
            if target == 0 :
                result.append(current_comb.copy())
                return 
            if ind == len(candidates):
                return 
            
            if candidates[ind] <= target:
                current_comb.append(candidates[ind])
                generatecombinations(ind, current_comb, target - candidates[ind])
                current_comb.pop()
            
            generatecombinations(ind + 1, current_comb, target)
        generatecombinations(0, [],target)
        return result