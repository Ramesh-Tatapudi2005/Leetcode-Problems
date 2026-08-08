class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                if stack and stack[-1] < -asteroids[i]:
                    stack.pop()
                elif stack  and stack[-1] == -asteroids[i]:
                    stack.pop()
                    i += 1
                else:
                    i += 1
            else:
                stack.append(asteroids[i])
                i += 1
        return stack