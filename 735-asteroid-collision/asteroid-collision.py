class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
       stack = []
       n = 0
       while n < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[n] < 0:
                if stack[-1] < abs(asteroids[n]):
                    stack.pop()
                elif stack[-1] == abs(asteroids[n]):
                    stack.pop()
                    n += 1
                else:
                    n += 1
            else:
                stack.append(asteroids[n])
                n += 1
       return stack