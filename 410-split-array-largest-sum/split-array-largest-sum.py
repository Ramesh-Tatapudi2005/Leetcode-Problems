class Solution:
    def CalcMax(self, nums, max_sum):
        ks = 1
        mx = 0
        for num in nums:
            if num + mx > max_sum:
                ks += 1
                mx = num
            else:
                mx += num
        return ks
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        noofk= 0
        while low <= high:
            mid = (low + high) // 2
            noofk = self.CalcMax(nums, mid)
            if noofk <= k:
                high = mid - 1
            else:
                low = mid + 1
        return low