class Solution:
    def checktemp(self, temp):
        left = temp[1] and temp[2] and temp[3] and temp[4]
        mid = temp[3] and temp[4] and temp[5] and temp[6]
        right = temp[5] and temp[6] and temp[7] and temp[8]
        if left and right:
            return 2
        if left or mid or right :
            return 1
        return 0
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedSeats.sort()
        # print(reservedSeats)
        length  = len(reservedSeats)
        ans= 0
        temp = [True] * 10
        cur_row = reservedSeats[0][0]
        prev_row = cur_row
        for i in range(length):
            row = reservedSeats[i][0]
            seat = reservedSeats[i][1]
            if row != cur_row:
                ans += self.checktemp(temp)
                ans += (row - cur_row-1 ) * 2
                cur_row = row
                temp = [True] * 10
            temp[seat-1] = False
        ans += self.checktemp(temp)
        ans += (n - cur_row ) * 2
        ans += (reservedSeats[0][0] - 1) * 2
        return ans
