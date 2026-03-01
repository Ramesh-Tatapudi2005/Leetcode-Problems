class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i ,num in enumerate(nums):
            dif = target - num 
            print(i,num,dif)
            if dif in h:
                return [h[dif],i] 
            h[num] = i