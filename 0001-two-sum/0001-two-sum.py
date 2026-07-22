class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            current_sum=target-nums[i]
            if current_sum in seen:
                return [seen[current_sum],i]
            seen[nums[i]]=i
        