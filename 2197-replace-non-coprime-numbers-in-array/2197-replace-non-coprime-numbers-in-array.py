class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        result=[]
        for nums in nums:
            result.append(nums)
            while len(result) >= 2:
                x=result[-2]
                y=result[-1]
                common_divisor=gcd(x,y)
                if common_divisor>1:
                    result.pop()
                    result.pop()
                    result.append(lcm(x,y))
                else:
                    break
        return result

