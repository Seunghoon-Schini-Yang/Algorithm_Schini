import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def adjs(r, c):
    if 0 < r:  yield r-1, c
    if 0 < c:  yield r, c-1
    if r < n-1:  yield r+1, c
    if c < n-1:  yield r, c+1


def dfs(r, c):
    maxy = 0
    for rr, cc in adjs(r, c):
        if forest[rr][cc] <= forest[r][c]:
            continue
        if memo[rr][cc]:
            maxy = max(maxy, memo[rr][cc])
        else:
            maxy = max(maxy, dfs(rr, cc))
    memo[r][c] = maxy + 1
    return memo[r][c]


if __name__ == '__main__':
    n = int(input())
    forest = [list(map(int, input().split())) for _ in range(n)]
    memo = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if memo[r][c]:
                continue
            dfs(r, c)
    print(max(max(r) for r in memo))
