class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for ch in s:
            if ch.isalpha() or ch.isdigit():
                temp += ch.lower()
        left = 0
        right = len(temp)-1
        while left <= right:
            if temp[left] != temp[right]:
                return False
            left += 1
            right -= 1
        return True