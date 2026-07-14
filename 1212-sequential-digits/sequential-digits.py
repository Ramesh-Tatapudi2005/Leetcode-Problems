class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = ["1","2","3","4","5","6","7","8","9"]
        res = []
        lowlen = len(str(low))
        highlen = len(str(high))
        j = int(str(low)[0])
        for i in range(lowlen,highlen+1):
            while (j-1)+ i <= 9:
                num = int("".join(digits[(j-1):(j-1)+i])) 
                print(num)
                if num >= low and num <= high:
                    res.append(num)
                j +=1
            j = 1
        return res