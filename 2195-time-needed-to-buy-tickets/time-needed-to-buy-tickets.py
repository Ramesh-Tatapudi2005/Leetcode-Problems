from collections import deque
class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        req = tickets[k]
        queue = deque([x for x in range(len(tickets))])
        ans = 0
        while tickets[k] != 0:
            tickets[queue[0]] -= 1
            if tickets[queue[0]] == 0:
                queue.popleft()
            else:
                queue.append(queue.popleft()) 
            ans += 1
        return ans