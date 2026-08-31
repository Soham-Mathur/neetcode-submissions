class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return False
        cycle_count = 0
        while n !=1 and cycle_count < 40:
            cycle_count += 1
            x = 0
            while n != 0:
                y = n % 10 
                x += y**2
                n //= 10
            n = x
        if n == 1:
            return True
        else:
            return False