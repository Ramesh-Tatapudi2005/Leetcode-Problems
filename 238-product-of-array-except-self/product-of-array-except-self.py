class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pro = 1
        zeros = 0
        ans = [0] * n
        for num in nums:
            if num !=0:
                pro *= num
            else:
                zeros += 1
        if zeros > 1:
            return ans
        if zeros == 1:
            for i in range(n):
                if nums[i] == 0:
                    ans[i] = pro
                else:
                    ans[i] = 0
            return ans
        else:
            return [pro // num for num in nums]