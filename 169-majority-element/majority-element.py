class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand = None
        count = 0
        for can in nums:
            if count == 0:
                cand = can
            if can == cand:
                count += 1
            else:
                count -= 1
        return cand