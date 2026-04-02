from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for b in bills:
            if b == 20:
                if change[10] > 0:
                    change[10] -= 1
                    change[5] -= 1
                else:
                    change[5] -= 3
            elif b == 10:
                change[5] -= 1
                change[10] += 1
            else:
                change[5] += 1

            if change[5] < 0 or change[10] < 0:
                return False
        
        return True
