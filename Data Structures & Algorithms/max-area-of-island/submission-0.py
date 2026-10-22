class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        DIRS = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        maxarea = 0


        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            area = 1
            while q:
                row,col = q.popleft()
                for dr,dc in DIRS:
                    nr,nc = row+dr,col+dc
                    if (nr<0 or nr >= ROWS or nc < 0 or nc >= COLS
                        or grid[nr][nc]==0 or (nr,nc) in visited):
                        continue
                    visited.add((nr,nc))
                    q.append((nr,nc))
                    area+=1
            return area



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = bfs(r,c)
                    maxarea = max(maxarea,area)

        return maxarea


