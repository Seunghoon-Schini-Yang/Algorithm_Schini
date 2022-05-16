import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    INF = sys.maxsize

    rgb = map(int, input().split())
    memo = [[INF]*3 for i in range(3)]
    for i in range(3):
        memo[i][i] = next(rgb)
    
    for i in range(n-1):
        rgb = tuple(map(int, input().split()))
        for f_c in range(3):
            to_paint = (min(memo[f_c][1], memo[f_c][2]), min(memo[f_c][2], memo[f_c][0]), min(memo[f_c][0], memo[f_c][1]))
            memo[f_c][:] = [cur+pre for cur, pre in zip(rgb, to_paint)]

    return min(memo[i][j] for j in range(3) for i in range(3) if i != j)


print(sol(int(input())))
