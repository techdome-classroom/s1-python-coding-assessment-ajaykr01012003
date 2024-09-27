class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Check if the grid is empty
        if not grid:
            return 0

        # Helper function to perform DFS and mark visited land cells
        def dfs(i: int, j: int):
            # Base case: if out of bounds or the current cell is water ('W')
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 'W':
                return
            # Mark the current cell as visited by turning it into water ('W')
            grid[i][j] = 'W'
            # Explore the neighboring cells (up, down, left, right)
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # Initialize island count
        island_count = 0

        # Traverse the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If we encounter land ('L'), it's a new island
                if grid[i][j] == 'L':
                    # Perform DFS to mark the entire island
                    dfs(i, j)
                    # Increment the island count
                    island_count += 1

        return island_count
