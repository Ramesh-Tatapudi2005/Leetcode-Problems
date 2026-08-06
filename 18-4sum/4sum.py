class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        res = []
        Sum = 0
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i+1,n):
                if j > i +1 and nums[j] == nums[j-1]:continue
                l = j + 1
                k = n -1
                while l < k:
                    Sum = nums[i] + nums[j] + nums[l] + nums[k]
                    if Sum < target:
                        l += 1
                    elif Sum > target:
                        k -= 1
                    else:
                        res.append([nums[i] , nums[j] , nums[l] , nums[k]])
                        l += 1
                        k -= 1
                        while l < k and nums[l] == nums[l-1]: l += 1
                        while l < k and nums[k] == nums[k+1]: k -= 1
        return res