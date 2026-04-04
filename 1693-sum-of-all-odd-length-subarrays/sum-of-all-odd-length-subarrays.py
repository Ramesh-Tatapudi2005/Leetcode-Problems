class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = sum(arr)
        temp = []
        t = 0
        for i in arr:
            t += i
            temp.append(t)
        for i in range(2,len(temp),2):
            for j in range(i,len(temp)):
                if i == j:
                    res += temp[j]
                else:
                    res += temp[j] - temp[j-i-1]
        return res