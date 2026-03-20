from typing import List

class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = []
        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):
                arr = set()
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        arr.add(grid[x][y]) 
                arr = sorted(arr)
                if len(arr) == 1:
                    row.append(0)
                else:
                    mn = float('inf')
                    for t in range(1, len(arr)):
                        mn = min(mn, arr[t] - arr[t-1])
                    row.append(mn)

            res.append(row)

        return res