def solution(msize):
    mlen = len(msize)
    size = [s for s, _ in msize]
    size.append(msize[-1][-1])
    memo = [[0]*mlen for _ in range(mlen)]
    for i in range(1, mlen):
        for j in range(i):
            x, y = i-1-j, i
            memo[x][y] = min(size[x]*size[k+1]*size[y+1] + memo[x][k] + memo[k+1][y] for k in range(x, y))
    return memo[0][-1]
