class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        s=set()
        for i in range(len(nums)-1):
            current_sum=nums[i]+nums[i+1]
            if current_sum in s:
                return True
            s.add(current_sum)
            
        return False
          