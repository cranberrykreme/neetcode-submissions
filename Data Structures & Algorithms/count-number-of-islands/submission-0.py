class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count_num_i = 0
        visited = set()
        for row in range(rows):
            for col in range(cols):
                if (row, col) in visited:
                    continue
                if grid[row][col] == '1':
                    count_num_i += 1
                stack = deque([(row,col)])
                while stack:
                    r, c = stack.popleft()
                    visited.add((r,c))
                    if grid[r][c] == '1':
                        if r > 0 and (r-1, c) not in visited:
                            stack.append((r-1, c))
                        if c > 0 and (r, c-1) not in visited:
                            stack.append((r, c-1))
                        if r < rows-1 and (r+1, c) not in visited:
                            stack.append((r+1, c))
                        if c < cols-1 and (r, c+1 not in visited):
                            stack.append((r, c+1))
        return count_num_i

