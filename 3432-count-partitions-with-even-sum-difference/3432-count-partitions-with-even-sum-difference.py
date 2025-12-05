class Solution:
    def countPartitions(self, nums):
        total = sum(nums)
        return len(nums)-1 if total % 2 == 0 else 0