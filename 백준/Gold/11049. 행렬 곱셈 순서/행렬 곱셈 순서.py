# teferi00 님 코드 참고
# dynamic programming + zip iterator
import sys
input = sys.stdin.readline

def sol(n: int) -> int:
    size_dp = [0]*(n+1)
    val_dp = [[0]*n for _ in range(n)]
    for i in range(n-1):
        size_dp[i] = next(map(int, input().split()))
    size_dp[n-1] ,size_dp[n] = map(int, input().split())

    for gap in range(1,n):
        for i in range(n-gap):
            j = i+gap
            size_ij = size_dp[i]*size_dp[j+1]
            # val_dp[i][j] = min(size_ij*size_dp[k+1] + val_dp[i][k] + val_dp[k+1][j] for k in range(i,j))
            val_dp[i][j] = val_dp[j][i] = min(size_ij*size_k + front + back for size_k,front,back in zip(size_dp[i+1:j+1],val_dp[i][i:j],val_dp[j][i+1:j+1]))

    return val_dp[0][n-1]


print(sol(int(input())))
