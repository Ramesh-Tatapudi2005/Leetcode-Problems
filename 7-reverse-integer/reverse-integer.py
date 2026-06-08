class Solution:
    def reverse(self, x: int) -> int:
        # st = str(x)
        # res = ""
        # if st[0] == '-':
        #     temp = st[::-1].lstrip('0')
        #     n = len(temp)
        #     res = "-" + temp[:n-1]
        # else:
        #     res = st[::-1].lstrip('0')
        # return int(res) if res and int(res) < 2**31 -1 and int(res) > -2**31   else 0

        sign = -1 if x < 0 else 1
        res = 0
        x = abs(x)
        while x != 0:
            rem = x % 10 
            res = rem + res * 10
            x = x // 10
        res *= sign
        if res < -2**31 or res > 2**31 -1:
            return 0
        return res