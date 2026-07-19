class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        ans = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= nums[low]:
                ans = min(nums[low], ans)
                low = mid +1
            else:# nums[mid] <= nums[hig]
                ans = min(nums[mid],ans)
                high = mid - 1
        return ans