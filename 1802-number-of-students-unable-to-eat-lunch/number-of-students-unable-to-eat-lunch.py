from collections import deque
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # cnt0 = students.count(0)
        # cnt1 = students.count(1)
        # for i, s in enumerate(sandwiches):
        #     if s == 1:
        #         if cnt1 == 0:
        #             return len(sandwiches) - i
        #         cnt1 -= 1
        #     else:
        #         if s == 0:
        #             if cnt0 == 0:
        #                 return len(sandwiches) - i
        #         cnt0 -= 1
        # return 0

        q = deque(students)
        i = 0
        f = 0
        while q and f < len(q):
            if q[0] == sandwiches[i]:
                q.popleft()
                i += 1
                f = 0
            else:
                q.append(q.popleft())
                f += 1
        return len(q)