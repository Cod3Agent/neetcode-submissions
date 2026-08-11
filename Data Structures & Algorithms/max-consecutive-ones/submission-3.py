class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        total = 0
        greatest = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                total += 1
            if nums[i] == 0:
                total = 0
            if nums[i] == 0 and total > greatest:
                greatest = total
            if total > greatest:
                greatest = total
        return greatest