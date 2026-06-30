class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a':0,'b':0,'c':0}
        i = j = 0
        n = len(s)
        ans =0
        while j< n:
            d[s[j]] += 1
            while d['a'] >0 and d['b'] > 0 and d['c'] > 0:
                ans += n-j
                d[s[i]] -= 1
                i += 1
            j+=1
        return ans