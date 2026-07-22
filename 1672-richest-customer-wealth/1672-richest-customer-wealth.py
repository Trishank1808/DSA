class Solution:
    def maximumWealth(self, account: List[List[int]]) -> int:
        max_wealth = 0
        for customer in account:
            total = 0
            for account in customer:
                total+=account
            if total > max_wealth:
                max_wealth=total
        return max_wealth