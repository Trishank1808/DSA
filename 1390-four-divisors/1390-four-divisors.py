class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total_sum = 0
        for n in nums:
            count = 0
            div_sum = 0
            for i in range(1, int(n**0.5) + 1):
                if n % i == 0:
                    j = n // i
                    count += 1
                    div_sum += i
                    if i != j:
                        count += 1
                        div_sum += j
                if count > 4:
                    break
            if count == 4:
                total_sum += div_sum
        return total_sum
