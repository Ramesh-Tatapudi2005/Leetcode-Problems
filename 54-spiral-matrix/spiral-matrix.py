class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top  = left = 0
        right , bottom = len(matrix[0])-1, len(matrix)-1
        ans = []
        while top <= bottom and left <= right:
            for l in range(left,right+1):
                ans.append(matrix[left][l])
            top +=1 

            for r in range(top, bottom+1):
                ans.append(matrix[r][right])
            right -=1 

            if top <= bottom:
                for b in range(right,left-1,-1):
                    ans.append(matrix[bottom][b])
                bottom-=1
            if left<= right:
                for t in range(bottom, top-1,-1):
                    ans.append(matrix[t][left])
                left+=1
            print("last",ans)
        return ans