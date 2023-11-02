import sys
input = sys.stdin.readline


def main():
    N, K = map(int, input().split())
    dist = [list(map(int, input().split())) for _ in range(N)]
    for m in range(N):
        for i in range(N):
            if i == m:
                continue
            for j in range(N):
                if j == m:
                    continue
                dist[i][j] = min(dist[i][j], dist[i][m] + dist[m][j])

    memo = [[sys.maxsize] * N for _ in range(2**N)]
    memo[1<<K][K] = 0
    que = [(1<<K, K)]
    while que:
        tmp = []
        for mask, loc in que:
            for i in range(N):
                if mask & (1<<i):
                    continue
                new = mask|(1<<i)
                if memo[mask][loc] + dist[loc][i] < memo[new][i]:
                    memo[new][i] = memo[mask][loc] + dist[loc][i]
                    tmp.append((new, i))
        que = tmp
    print(min(memo[-1]))


if __name__ == '__main__':
    main()
