import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    INF = sys.maxsize

    time_table = [[INF]*n for _ in range(n)]
    for i in range(n):
        time_table[i][i] = 0
    for _ in range(m):
        a,b,c = map(int, input().split())
        if c < time_table[a-1][b-1]:
            time_table[a-1][b-1] = c

    for i in range(n):
        for j in range(n):
            if i==j or time_table[j][i]==INF:
                continue
            for k in range(n):
                if i==k:
                    continue
                if time_table[j][i]+time_table[i][k] < time_table[j][k]:
                    time_table[j][k] = time_table[j][i]+time_table[i][k]

    return '\n'.join(' '.join('0' if d==INF else str(d) for d in line) for line in time_table)


print(sol(int(input()), int(input())))
