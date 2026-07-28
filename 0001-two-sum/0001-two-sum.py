class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans={}
        for i in range(len(nums)):
            need=target-nums[i]
            if need in ans:
                return [ans[need],i]
            ans[nums[i]]=i

        
            
    