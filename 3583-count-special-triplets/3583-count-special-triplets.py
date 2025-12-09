class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        left = Counter()
        right = Counter(nums)
        ans = 0

        for j in range(len(nums)):
            right[nums[j]] -= 1
            required = nums[j] * 2
            ans = (ans + left[required] * right[required]) % MOD
            left[nums[j]] += 1

        return ans % MOD