class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            time = (target-position[i]) / speed[i]
            cars.append((position[i], time))
        cars.sort(reverse=True)
        fleet = 0
        fleet_speed = 0
        
        for pos , time in cars:
            if fleet_speed < time:
                fleet += 1
                fleet_speed = time
        return fleet