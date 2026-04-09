class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        ind = word.index(ch)
        l = list(word)
        s1 = "".join(reversed(l[0:ind+1]))
        s2 = "".join(l[ind+1:])
        return s1+ s2