class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        max_row = [0] * (n + 1)
        min_row = [n + 1] * (n + 1)
        max_col = [0] * (n + 1)
        min_col = [n + 1] * (n + 1)

        for x, y in buildings:
            min_row[x] = min(min_row[x], y)
            max_row[x] = max(max_row[x], y)
            min_col[y] = min(min_col[y], x)
            max_col[y] = max(max_col[y], x)
        res = 0
        for x, y in buildings:
            if (min_row[x] < y < max_row[x] and
                min_col[y] < x < max_col[y]):
                res += 1
        return res
