import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> int:
    origin_state = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    return clean(grid, [*origin_state, 0])


def clean(grid: list, state: list) -> int:
    cleaned = 0
    grid[state[0]][state[1]] = 2
    if state[2] == 1:
        state[2] = 3
    elif state[2] == 3:
        state[2] = 1

    while state:
        r,c,dir,cls = state
        if not cls:
            cleaned += 1
        
        not_moved = True
        for i in range(dir+1, dir+5):
            nr = r+dr[i]; nc = c+dc[i]
            if not grid[nr][nc]:
                grid[nr][nc] = 2
                state = [nr, nc, i%4, 0]
                not_moved = False
                break
                
        if not_moved:
            i = (i+2)%4
            nr = r+dr[i]; nc = c+dc[i]
            if grid[nr][nc] == 1:
                return cleaned
            state = [nr, nc, dir, grid[nr][nc]]
            grid[nr][nc] = 2
        


if __name__ == '__main__':
    dr = [-1, 0, 1, 0, -1, 0, 1, 0]
    dc = [0, -1, 0, 1, 0, -1, 0, 1]
    print(sol(*map(int, input().split())))
