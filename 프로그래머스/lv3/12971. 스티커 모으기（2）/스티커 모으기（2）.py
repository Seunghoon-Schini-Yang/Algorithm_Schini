def solution(sticker):
    n = len(sticker)
    if n == 1:
        return sticker[0]
    memo = [[0, 0] for _ in range(n)]
    memo[0][0] =  memo[1][0] = sticker[0]
    memo[1][1] = sticker[1]
    for i in range(2, n):
        for j in range(2):
            memo[i][j] = max(memo[i-2][j] + sticker[i], memo[i-1][j])
    return max(memo[-2][0], memo[-1][1])
