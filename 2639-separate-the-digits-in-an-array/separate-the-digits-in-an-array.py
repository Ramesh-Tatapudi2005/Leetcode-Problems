class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        s = ""
        for i in nums:
            s += str(i)
        l = []
        for i in s:
            l.append(int(i))
        return l