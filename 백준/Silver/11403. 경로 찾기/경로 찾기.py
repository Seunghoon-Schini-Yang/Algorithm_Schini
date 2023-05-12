import sys
input = sys.stdin.readline


def dfs(nn):
    if is_visit[nn]:
        return conn[nn]
    is_visit[nn] = True
    new = conn[nn].copy()
    for cn in new:
        conn[nn] |= dfs(cn)
    return conn[nn]


if __name__ == '__main__':
    N = int(input())
    is_visit = [False] * N
    conn = [set() for _ in range(N)]
    for i in range(N):
        for j, v in enumerate(map(int, input().split())):
            if not v:
                continue
            conn[i].add(j)

    for i in range(N):
        is_visit[i] = False
        dfs(i)

    print('\n'.join(' '.join('1' if j in conn[i] else'0' for j in range(N)) for i in range(N)))
