class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        MOD=12345
        m,n=len(grid),len(grid[0])
        p=[[0] *n for _ in range(m)]
        prod=1
        suffix=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                p[i][j]=suffix
                suffix = (suffix * grid[i][j]) % MOD
        prefix=1
        for i in range(m):
            for j in range(n):
                p[i][j]=(p[i][j]*prefix)% MOD
                prefix = (prefix * grid[i][j]) % MOD
        return p


        