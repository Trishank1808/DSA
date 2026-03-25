class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        total_sum=sum(sum(row)for row in grid)
        if total_sum%2!=0:
            return False
        target =total_sum//2
        curr_sum=0
        for i in range(m):
            curr_sum+=sum(grid[i])
            if curr_sum==target:
                return True
        curr_sum=0
        for j in range(n):
            curr_sum += sum(grid[i][j] for i in range(m))
            if curr_sum==target:
                return True
        return False
