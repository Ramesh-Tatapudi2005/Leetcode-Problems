class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def generatepermut(ind, curr_perm, unused):
            if len(curr_perm) == n:
                result.append(curr_perm.copy())
                return 
            
            for i in range(n):
                if unused[i]: continue

                curr_perm.append(nums[i])
                unused[i] = not unused[i]
                generatepermut(i+1, curr_perm, unused)
                curr_perm.pop()
                unused[i] = not unused[i]

        unused = [False] * n
        generatepermut(0, [], unused)
        return result