class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        s = sorted(strs)
        f = s[0]
        l = s[-1]
        m = len(f)
        for i in range(m):
            if f[i] != l[i]:
                return ans
            ans += f[i]
        return ans