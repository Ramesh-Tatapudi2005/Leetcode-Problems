class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        left = right = 0
        ans = float('-inf')
        # while right < len(nums):
        #     if nums[right] == 0:
        #         zeros += 1
        #     while zeros > k:
        #         if nums[left] == 0:
        #             zeros -= 1
        #         left += 1
        #     ans = max(ans, right- left + 1)
        #     right += 1
        # return ans
        while right < len(nums):
            if nums[right] == 0:
                zeros += 1
            if zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1
        return ans