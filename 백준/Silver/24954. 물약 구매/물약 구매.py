import sys
input = sys.stdin.readline


def dfs(cur_sum: int, mask: int) -> None:
    global cost

    if memo[mask] <= cur_sum:
        return
    memo[mask] = cur_sum

    for i in range(N):
        if not mask&(1<<i):
            tmp = cost[:]
            for k,v in discnt[i].items():
                cost[k] = cost[k]-v if cost[k] > v else 1
            dfs(cur_sum+cost[i], mask|(1<<i))
            cost = tmp
    return


if __name__ == '__main__':
    N = int(input())
    cost = list(map(int, input().split()))
    discnt = [dict() for _ in range(N)]
    for i in range(N):
        for _ in range(int(input())):
            a,d = map(int, input().split())
            discnt[i][a-1] = d

    INF = 10_000
    memo = [INF]*(1<<N)
    dfs(0, 0)
    print(memo[(1<<N)-1])
