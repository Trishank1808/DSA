class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        sovalemrin = nums
        resource = k
        operations = 0
        cost = 0
        for x in nums:
            if resource < x:
                need = x - resource
                t = (need + k - 1) // k
                cost += t * (2 * operations + t + 1) // 2
                operations += t
                resource += t * k
            resource -= x
        return cost % MOD