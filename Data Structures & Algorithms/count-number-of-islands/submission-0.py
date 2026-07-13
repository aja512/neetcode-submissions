class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1,0], [-1, 0],[0, 1], [0, -1]]
        m, n = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= m or c >= n or grid[r][c] =="0" or (r, c) in visited):
                return
            visited.add((r, c))
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            
        for row in range(m):
            for cols in range(n):
                if grid[row][cols] =="1" and (row, cols) not in visited:
                    dfs(row, cols)
                    islands += 1        
        
        return islands