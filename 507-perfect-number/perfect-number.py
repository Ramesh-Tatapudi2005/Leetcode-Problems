import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # s = 1
        # if num == 1 or num == 0:
        #     return False
        # for i in range(2,int(math.sqrt(num))+1):
        #     if num % i == 0:
        #         s = s + i + (num//i)
        # return (s==num)
        return num in [6,28,496,8128,33550336,8589869056]