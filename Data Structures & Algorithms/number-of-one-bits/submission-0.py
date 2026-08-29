class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            last = n % 2
            if last == 1:
                total += 1
            n //= 2
        return total