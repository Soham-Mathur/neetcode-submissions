class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        anchor = 0
        for num in range(anchor+1, len(nums)):
            if nums[num] == nums[anchor]:
                return True
            else:
                anchor += 1
        return False