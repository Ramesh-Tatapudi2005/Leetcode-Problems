class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        s = len(set(nums))
        has = {}
        n = len(nums)
        i = j = 0
        ans = 0
        while i <= j and i < n:
            while len(has.keys()) < s and j < n:
                has[nums[j]] = has.get(nums[j], 0) + 1
                j += 1
            if len(has.keys()) == s:
                ans += n - (j-1)
            if has[nums[i]] == 1:
                del has[nums[i]]
            else:
                has[nums[i]] -= 1
            i += 1
        return ans