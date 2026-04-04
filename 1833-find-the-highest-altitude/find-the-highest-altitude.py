class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        pre = [0] * len(gain)
        pre[0] = 0
        for i in gain:
            pre.append(pre[-1] + i)
        return max(pre)