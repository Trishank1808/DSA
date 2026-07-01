from collections import deque
from typing import List

class Solution:
    dir = [(1,0), (-1,0), (0,1), (0,-1)]

    def isValidCell(self, grid, i, j):
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

    def isValidSafeness(self, grid, safeness):
        n = len(grid)

        if grid[0][0] < safeness:
            return False

        q = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        visited[0][0] = True

        while q:
            i, j = q.popleft()

            if i == n - 1 and j == n - 1:
                return True

            for di, dj in self.dir:
                ni, nj = i + di, j + dj

                if (self.isValidCell(grid, ni, nj)
                        and not visited[ni][nj]
                        and grid[ni][nj] >= safeness):
                    visited[ni][nj] = True
                    q.append((ni, nj))

        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        multi_source_queue = deque()

        # Step 1: Add all thieves to queue
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    multi_source_queue.append((i, j))
                    grid[i][j] = 0
                else:
                    grid[i][j] = -1

        # Step 2: Multi-Source BFS
        while multi_source_queue:
            i, j = multi_source_queue.popleft()

            for di, dj in self.dir:
                ni, nj = i + di, j + dj

                if self.isValidCell(grid, ni, nj) and grid[ni][nj] == -1:
                    grid[ni][nj] = grid[i][j] + 1
                    multi_source_queue.append((ni, nj))

        # Step 3: Binary Search
        start = 0
        end = max(max(row) for row in grid)
        ans = 0

        while start <= end:
            mid = (start + end) // 2

            if self.isValidSafeness(grid, mid):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1

        return ans