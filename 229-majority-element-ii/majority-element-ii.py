class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dic = {}
        n = len(nums)
        minim = n// 3
        ans = []
        for num in nums:
            dic[num] = dic.get(num,0)+1
            # print(dic[num])
            if dic[num] > minim and num not in ans:
                print(2)
                ans.append(num)
            if num not in ans and dic[num] == n:
                print(1)
                ans.append(num)
        return ans