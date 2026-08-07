from bisect import bisect_left
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # right = bisect_left(arr, x)
        # left = right -1

        # while k :
        #     if left < 0:
        #         right += 1
        #     elif right >= len(arr):
        #         left -= 1
        #     elif abs(arr[left]- x) <= abs(arr[right]-x):
        #         left -= 1
        #     else:
        #         right += 1
        # return arr[left+1:right]

        low = 0
        high = len(arr) - k
        while low < high:
            mid = (low+ high) // 2
            
            if x - arr[mid] > arr[mid+k]-x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]