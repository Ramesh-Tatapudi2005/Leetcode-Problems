class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        Hash = {0:1}
        prefsum = 0
        ans = 0
        for i in range(len(nums)):
            prefsum += nums[i]
            diff = prefsum - k
            if diff in Hash:
                ans += Hash[diff]
            Hash[prefsum] = Hash.get(prefsum,0)+1
        return ans