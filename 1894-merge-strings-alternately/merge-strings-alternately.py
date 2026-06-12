class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        l =  r = 0
        while l < len(word1) and r < len(word2):
            res = res + word1[l] + word2[r]
            l += 1
            r += 1
        if r < len(word2):
            return res + word2[r:]
        if l < len(word1):
            return res + word1[l:]
        return res