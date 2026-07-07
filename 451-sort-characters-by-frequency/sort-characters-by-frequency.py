from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        res = ""
        dic = dict(sorted(dic.items(), key = lambda x : x[1],reverse = True))
        print(dic)
        for k,v in dic.items():
            res += k * v
            print
        return res
        