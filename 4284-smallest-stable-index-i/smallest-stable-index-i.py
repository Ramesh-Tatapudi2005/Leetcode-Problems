class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        pref = [0] * n
        suf = [0] * n
        ans = float('inf')
        Max, Min = 0, float('inf')
        j = n - 1
        for i in range(n):
            if nums[i] > Max:
                Max = nums[i]
            if nums[j] < Min:
                Min = nums[j]
            pref[i], suf[j] = Max, Min 
            j -= 1
        print(pref, suf)
        for i in range(n):
            if pref[i] - suf[i] <= k:
                ans = min(i, ans)
        return ans if ans != float('inf') else -1