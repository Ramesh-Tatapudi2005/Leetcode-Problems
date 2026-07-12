class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31 -1
        i = 0
        n = len(s)
        sign = 1
        num = 0
        while i < n and s[i] == " ":
            i +=1
        if i == n :
            return 0
        if (s[i] == '+' or s[i] == '-'):
            sign = -1 if s[i] == '-' else 1
            i +=1 

        while i < n and s[i].isdigit():
            digit = int(s[i])

            if num > INT_MAX  // 10 or (num == INT_MAX // 10 and digit > 7 ):
                return INT_MAX if sign == 1 else INT_MIN
            num = num * 10 + digit
            i += 1

        return num * sign