import sys
input = sys.stdin.readline


def dfs(depth, p, r, c):
    global tp
    if depth == N:
        return
    for i in range(4):
        rr, cc = r+dr[i], c+dc[i]
        if not dirs[i]:
            continue
        if visit[rr][cc]:
            tp += p * dirs[i]
            continue
        visit[rr][cc] = True
        dfs(depth+1, p*dirs[i], rr, cc)
        visit[rr][cc] = False
    return


if __name__ == '__main__':
    N, *dirs = map(int, input().split())
    dirs = list(map(lambda x: x/100, dirs))
    dr, dc = [0, 0, 1, -1], [1, -1, 0, 0]
    visit = [[False] * ((N<<1)^1) for _ in range((N<<1)^1)]
    visit[0][0] = True
    tp = 0.0
    dfs(0, 1, 0, 0)
    print(1-tp)
    