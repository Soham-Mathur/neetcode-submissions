class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if high == 0:
            return 0
        while low % 2 == 1:
            low -= 1
        while high % 2 ==1:
            high +=1
        return (high - low)//2 