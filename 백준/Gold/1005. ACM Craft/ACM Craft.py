import sys
input = sys.stdin.readline


def testcase(N, K):
    cost = [0] + list(map(int, input().split()))
    dgr = [0] * (N+1)
    memo = [0] * (N+1)
    graph = [[] for _ in range(N+1)]
    for _ in range(K):
        p, c = map(int, input().split())
        graph[p].append(c)
        dgr[c] += 1
    W = int(input())
    q = [i for i in range(1, N+1) if not dgr[i]]
    while q:
        p = q.pop()
        if p == W:
            return str(cost[p])
        for c in graph[p]:
            memo[c] = max(memo[c], cost[p])
            dgr[c] -= 1
            if not dgr[c]:
                q.append(c)
                cost[c] += memo[c]


if __name__ == '__main__':
    print('\n'.join(testcase(*map(int, input().split())) for _ in range(int(input()))))
