class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_set=set()
        count=0
        for num in nums:
            if num in num_set:
                count=num
            num_set.add(num)
        for i in range(1,len(nums)+1):
            if i not in num_set:
                return[count,i]   
                

   