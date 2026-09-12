class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def generateSubsets(ind, current_sub_set):
            if ind >= len(nums):
                result.append(current_sub_set.copy())
                return 
            
            generateSubsets(ind+1 , current_sub_set)
            current_sub_set.append(nums[ind])
            generateSubsets(ind+1, current_sub_set)

            current_sub_set.pop()
                    
        generateSubsets(0, [])
        return result