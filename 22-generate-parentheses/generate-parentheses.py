class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def generate_paran(curr_paran, open, close , n):
            if len(curr_paran) == 2 * n:
                result.append(curr_paran)
                return 
            if open < n:
                generate_paran(curr_paran + "(", open + 1, close, n)
            if close < open:
                generate_paran(curr_paran+ ")", open , close + 1, n)
        generate_paran("",0,0, n)
        return result 