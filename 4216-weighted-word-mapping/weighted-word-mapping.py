class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        st = ""
        ind = 0
        ch = ""
        for i in words:
            s = 0
            for j in i:
                ind = ord(j) - ord('a')
                s += weights[ind]
            ch = chr(ord('z') - (s%26))
            st += ch
        return st