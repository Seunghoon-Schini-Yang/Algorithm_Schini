import sys
input = sys.stdin.readline


def dfs(mask: int, a_sum: int, ac_sum: int, p_sum: int) -> None:
    if a_sum >= memo[mask]:
        return
    memo[mask] = a_sum
    p_memo[mask] = p_sum
    
    for i in range(N):
        if not mask&(1<<i):
            dfs(mask|(1<<i), a_sum+ac_sum+attack[i], ac_sum+attack[i], p_sum+popul[i])
    return


if __name__ == '__main__':
    N,K = map(int, input().split())
    attack = list(map(int, input().split()))
    popul = list(map(int, input().split()))
    memo = [K+1]*(1<<N)
    p_memo = [0]*(1<<N)

    dfs(0, 0, 0, 0)
    print(max(p_memo))
