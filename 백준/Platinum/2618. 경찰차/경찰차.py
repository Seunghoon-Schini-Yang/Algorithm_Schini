# dynamic programming
# dp 1차원 배열
import sys
input = sys.stdin.readline

def sol(n: int, w: int) -> str:
    path_dp = [['']*2 for _ in range(w)]
    val_dp = [[0]*2 for _ in range(w)]
    locs = [(1,1)] + list(tuple(map(int, input().split())) for _ in range(w))

    val_dp[0][0], val_dp[0][1] = locs[1][0]+locs[1][1]-2, 2*n-locs[1][0]-locs[1][1]
    path_dp[0][0],path_dp[0][1] = '1','2'

    for i in range(2,w+1):
        miny_1 = miny_2 = sys.maxsize
        for j in range(i-1):
            gap_v = sum(abs(e1-e2) for e1,e2 in zip(locs[j],locs[i]))
            if val_dp[j][1] + gap_v < miny_1:
                miny_1 = val_dp[j][1] + gap_v
                path_cache_1 = path_dp[j][1]
            if not j:
                gap_v = sum(abs(e1-e2) for e1,e2 in zip((n,n),locs[i]))
            if val_dp[j][0] + gap_v < miny_2:
                miny_2 = val_dp[j][0] + gap_v
                path_cache_2 = path_dp[j][0]
            
            gap_h = sum(abs(e1-e2) for e1,e2 in zip(locs[i],locs[i-1]))
            val_dp[j][0] += gap_h
            val_dp[j][1] += gap_h

            path_dp[j][0] += '1'
            path_dp[j][1] += '2'

        val_dp[i-1][0], val_dp[i-1][1] = miny_1, miny_2
        path_dp[i-1][0] = path_cache_1 + '1'
        path_dp[i-1][1] = path_cache_2 + '2'

    miny = sys.maxsize
    for i in range(w):
        if val_dp[i][0] < miny:
            miny = val_dp[i][0]
            x,y = i,0
        if val_dp[i][1] < miny:
            miny = val_dp[i][1]
            x,y = i,1
    
    return str(miny)+'\n'+'\n'.join(path_dp[x][y])


print(sol(int(input()), int(input())))
