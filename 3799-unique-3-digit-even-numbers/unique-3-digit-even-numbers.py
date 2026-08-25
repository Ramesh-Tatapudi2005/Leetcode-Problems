from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        freq = Counter(digits)
        res = set()
        for last in freq.keys():
            if last % 2 == 1 or freq[last] == 0:
                continue
            freq[last] -= 1
            for first in freq.keys():
                if first == 0 or freq[first] == 0:
                    continue
                freq[first] -= 1
                for second in freq.keys():
                    if freq[second] == 0:
                        continue
                    else:
                        number = first * 100 + second * 10 + last
                        res.add(number)
                    print(first,last,number)
                freq[first] += 1
            freq[last] += 1
        print(res)
        return len(res)