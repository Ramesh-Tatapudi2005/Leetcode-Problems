from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        most_common = list(freq.most_common(k))
        ans = []
        for common in most_common:
            ans.append(common[0])
        return ans