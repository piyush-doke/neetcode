class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        lp, ls = position_speed[0]
        fleets = 1
        for p, s in position_speed[1:]:
            if (target - p) / s > (target - lp)/ ls:
                fleets += 1
                lp, ls = p, s
        return fleets