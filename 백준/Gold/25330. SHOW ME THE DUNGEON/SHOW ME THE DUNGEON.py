import sys
input = sys.stdin.readline


def dfs(mask: int, a_sum: int, ac_sum: int, p_sum: int) -> None:
    global maxy

    if a_sum >= memo[mask]:
        return
    if p_sum > maxy:
        maxy = p_sum
    memo[mask] = a_sum

    
    for i in range(N):
        if not mask&(1<<i):
            dfs(mask|(1<<i), a_sum+ac_sum+attack[i], ac_sum+attack[i], p_sum+popul[i])
    return


if __name__ == '__main__':
    N,K = map(int, input().split())
    attack = list(map(int, input().split()))
    popul = list(map(int, input().split()))
    memo = [K+1]*(1<<N)

    maxy = 0
    dfs(0, 0, 0, 0)
    print(maxy)
