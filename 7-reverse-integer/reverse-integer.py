class Solution:
    def reverse(self, x: int) -> int:
        st = str(x)
        res = ""
        if st[0] == '-':
            temp = st[::-1].lstrip('0')
            n = len(temp)
            res = "-" + temp[:n-1]
        else:
            res = st[::-1].lstrip('0')
        return int(res) if res and int(res) < 2**31 -1 and int(res) > -2**31   else 0
