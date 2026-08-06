class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right = 0, len(people) -1 
        people.sort()
        ans= 0
        # print(people)
        while left <= right:
            # print(people[left],people[right])
            if left == right:
                ans += 1
                left += 1
                right -= 1
            elif people[left] + people[right] <= limit:
                ans += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                ans += 1
                right -=1
        return ans
            