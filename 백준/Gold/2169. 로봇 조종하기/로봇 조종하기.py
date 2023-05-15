import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, M = map(int, input().split())

    prev = list(map(int, input().split()))
    for i in range(1, M):
        prev[i] += prev[i-1]

    for _ in range(N-1):
        cur = list(map(int, input().split()))
        l = [0] * M
        r = [0] * M
        l[0] = prev[0] + cur[0]
        r[~0] = prev[~0] + cur[~0]
        for i in range(1, M):
            l[i] = max(prev[i], l[i-1]) + cur[i]
            r[~i] = max(prev[~i], r[~(i-1)]) + cur[~i]
        prev = [max(ll, rr) for ll, rr in zip(l, r)]
    print(prev[-1])
