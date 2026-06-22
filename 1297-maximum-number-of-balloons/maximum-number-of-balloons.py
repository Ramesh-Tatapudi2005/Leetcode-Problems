from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        actmap = {'b':1,'a':1,'l': 2, 'o':2,'n':2}
        mini = float('inf')
        st = Counter(text)
        for i in actmap:
            if i == 'l' or i == 'o':
                mini =min(st[i]//2 , mini)
            mini = min(st[i], mini)
        return mini