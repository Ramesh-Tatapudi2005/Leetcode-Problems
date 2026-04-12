class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n = len(nums1)
        m = len(nums2)
        Sum = {}
        res =[]
        for i in nums1:
            Sum[i[0]] = i[1]
        for j in nums2:
            if j[0] in Sum:
                Sum[j[0]] += j[1]
            else:
                res.append(j)
        for k,v in Sum.items():
            res.append([k,v])
        return sorted(res,key = lambda x :x[0])