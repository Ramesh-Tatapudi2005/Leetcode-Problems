class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        n = len(nums)
        mid = n // 2
        leftsum = sum(nums[:mid])
        rightsum= sum(nums[mid: ])
        print(leftsum, rightsum)
        ans= 0
        if leftsum > rightsum:
            ans += 1
        for i in range(n-1):
            ind = (n-(mid-i))%n
            leftsum = leftsum + nums[ind]
            leftsum = leftsum - nums[i]
            rightsum = rightsum + nums[i] 
            rightsum = rightsum - nums[ind]
            print(leftsum, rightsum)
            if leftsum > rightsum:
                ans += 1
        
        return ans