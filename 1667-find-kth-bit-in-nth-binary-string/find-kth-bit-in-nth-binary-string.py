class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        pre = "0"
        s = ""
        for i in range(n-1):
            r = "".join(reversed(s.translate(str.maketrans("01","10")))) if len(pre) > 1 else str(1 - int(pre))
            s = pre + "1" + r
            pre = s
        return str(pre[k-1])