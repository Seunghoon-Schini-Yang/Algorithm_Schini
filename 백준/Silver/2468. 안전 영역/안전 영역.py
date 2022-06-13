import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def search(fall: int) -> int:
        def dfs(row: int, col: int):
            stack = [(row, col)]
            while stack:
                row, col = stack.pop()
                for i in range(4):
                    n_r = row+dr[i]; n_c = col+dc[i]
                    if 0 <= n_r < n and 0 <= n_c < n and grid[n_r][n_c] > fall and not visited[n_r][n_c]:
                        visited[n_r][n_c] = True
                        stack.append((n_r, n_c))
            return 1


        cnt = 0
        visited = [[False]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                if grid[row][col] > fall and not visited[row][col]:
                    cnt += dfs(row, col)
        return cnt

    
    grid = [list(map(int, input().split())) for _ in range(n)]
    # left, right, up, down
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    return max(search(fall) for fall in range(100))


print(sol(int(input())))
