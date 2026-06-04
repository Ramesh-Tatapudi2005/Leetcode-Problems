class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt0 = students.count(0)
        cnt1 = students.count(1)
        for i, s in enumerate(sandwiches):
            if s == 1:
                if cnt1 == 0:
                    return len(sandwiches) - i
                cnt1 -= 1
            else:
                if s == 0:
                    if cnt0 == 0:
                        return len(sandwiches) - i
                cnt0 -= 1
        return 0