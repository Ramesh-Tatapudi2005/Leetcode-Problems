class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        i = len(s) - 1
        word = ""
        while i >= 0:
            if s[i] != " ":
                word = s[i] + word
            elif s[i] == " " and word:
                if result:
                    result += " "
                result += word
                word = ""
            i -= 1
        if word:
            if result :
                result += " "
            result += word
        return result