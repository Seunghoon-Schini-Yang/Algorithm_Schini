import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> tuple:
    def melt_dfs(row: int, col: int) -> set:
        to_melt = list()
        stack = [(row, col)]
        while stack:
            zeros = 0
            row, col = stack.pop()
            for n_r, n_c in adjs(row, col):
                if not grid[n_r][n_c]:
                    zeros += 1
                elif (n_r, n_c) not in visited:
                    stack.append((n_r, n_c))
                    visited.add((n_r, n_c))
            if zeros:
                to_melt.append((row, col, zeros))

        new_iceberg = visited.copy()
        for row, col, zeros in to_melt:
            if grid[row][col] > zeros:
                grid[row][col] -= zeros
            else:
                grid[row][col] = 0
                new_iceberg.remove((row, col))
        return new_iceberg


    def adjs(row: int, col: int) -> tuple:
        yield row+1, col
        yield row-1, col
        yield row, col+1
        yield row, col-1

    
    iceberg = set()
    grid = [list(map(int, input().split()))]
    for row in range(1, n-1):
        grid.append(list(map(int, input().split())))
        for col in range(1, m-1):
            if grid[row][col]:
                iceberg.add((row, col))
    grid.append(list(map(int, input().split())))

    ans = 0
    while iceberg:
        row, col = iceberg.pop()
        visited = {(row, col)}
        new_iceberg = melt_dfs(row, col)

        if len(iceberg)+1 != len(visited):
            return ans
        
        iceberg = new_iceberg
        ans += 1
    return 0


print(sol(*map(int, input().split())))
