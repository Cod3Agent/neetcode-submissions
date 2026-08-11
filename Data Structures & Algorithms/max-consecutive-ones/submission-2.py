class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        greatest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                total += 1
            if nums[i] == 0:
                greatest = total
                total = 0
            if total > greatest:
                greatest = total
        return greatest