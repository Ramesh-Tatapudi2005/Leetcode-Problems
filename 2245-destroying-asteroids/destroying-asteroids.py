class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        m = max(asteroids)
        for i in asteroids:
            if mass < i:
                return False
            else:
                mass += i
                if mass >= m:
                    return True
        return True