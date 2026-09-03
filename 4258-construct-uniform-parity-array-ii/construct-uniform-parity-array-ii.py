class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        odd = float('inf')
        even = float('inf')
        for num in nums1:
            if num % 2 == 0:
                 even = min(even, num)
            else:
                odd = min(odd,num)
        # print(even,odd)
        if even < odd and even != float('inf') and odd != float('inf'):
            return False
        return True
