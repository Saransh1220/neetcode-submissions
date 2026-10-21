class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        land = 0
        visited = set()
        stack = []
        def dfs():
            row,col = stack.pop()
            for dr,dc in DIRS:
                nr,nc = row+dr,col+dc
                if (nr < 0 or nr>=ROWS or nc < 0 or nc >= COLS
                    or (nr,nc) in visited or grid[nr][nc]=='0'):
                    continue
                visited.add((nr,nc))
                stack.append((nr,nc))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r, c) not in visited:
                    land+=1
                    stack.append((r,c))
                    visited.add((r,c))
                    while stack:
                        dfs()
        
        return land