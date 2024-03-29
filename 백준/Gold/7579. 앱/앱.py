import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> int:
    memos = map(int, input().split())
    costs = map(int, input().split())
    dp = dict({0: 0})
    for cost, memo in zip(costs, memos):
        temp = dict()
        for ps_c in dp:
            if dp[ps_c] >= m:
                continue
            idx = ps_c+cost
            if dp.get(idx, 0) < dp[ps_c]+memo:
                temp[idx] = dp[ps_c]+memo
        for k, v in temp.items():
            dp[k] = v

    for i in range(10001):
        if dp.get(i, 0) >= m:
            return i

print(sol(*map(int, input().split())))
