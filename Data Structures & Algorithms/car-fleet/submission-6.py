class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = leader_time = 0
        for p, s in sorted(zip(position, speed), key=lambda x: x[0], reverse=True):
            if (time := (target - p) / s) > leader_time:
                fleets += 1
                leader_time = time
        return fleets