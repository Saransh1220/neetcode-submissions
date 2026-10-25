class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = collections.deque()

        # Start from every treasure chest
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        # BFS outward from all treasure chests
        while q:
            row, col = q.popleft()

            for dr, dc in DIRS:
                nr, nc = row + dr, col + dc

                if (nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    grid[nr][nc] != 2147483647):
                    continue

                grid[nr][nc] = grid[row][col] + 1
                q.append((nr, nc))