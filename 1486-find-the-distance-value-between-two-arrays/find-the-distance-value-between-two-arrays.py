from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        res = 0
        arr2.sort()
        for num in arr1:
            idx = bisect_left(arr2, num- d)
            print(idx)
            if idx == len(arr2) or arr2[idx] > num + d:
                res += 1
        return res