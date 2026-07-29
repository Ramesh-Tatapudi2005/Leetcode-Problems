class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        ans = float('inf')
        for l in range(n):
            j = l + 1
            k = n-1
            while j < k:
                tsum = nums[l] + nums[j]  + nums[k]
                if tsum == target:
                    return target
                elif tsum > target:
                    if abs(target-tsum) <= abs(target- ans):
                        ans = tsum
                    k -= 1
                else:
                    if abs(target - tsum) < abs(target - ans):
                        ans = tsum
                    j += 1
        return ans if ans != float('inf') else 0