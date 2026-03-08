from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        window = {}
        req = len(need)
        form = 0
        l = 0
        ans = float('inf'),0,0
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c,0) + 1
            if c in need and window[c] == need[c]:
                form +=1 

            while l <= r and req == form:
                if r - l + 1 < ans[0]:
                    ans = (r-l+1,l,r)
                c = s[l]
                window[c] -= 1
                if c in need and window[c] < need[c]:
                    form -= 1
                l += 1
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]