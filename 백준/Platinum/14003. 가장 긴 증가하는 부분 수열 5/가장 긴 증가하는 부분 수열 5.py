# dynamic programming
# bisect 로 level 이분 탐색하면 조금 더 빠를 듯
import sys
input = sys.stdin.readline
from bisect import bisect_left

def sol(n: int) -> str:
    seq = list(map(int, input().split()))
    dp = [[[0,seq[0]]]]
    lis = [seq[0]]
    level = 0
    lis_len = 1

    for v in seq[1:]:
        cur_idx = bisect_left(lis, v)
        if cur_idx == lis_len:
            lis.append(v)
            dp.append([[level,v]])
            lis_len += 1
        elif lis[cur_idx] == v:
            continue
        else:
            lis[cur_idx] = v
            level += 1
            dp[cur_idx].append([level,v])

    level = dp[-1][-1][0]
    ans = [0]*lis_len
    ans[-1] = str(dp[-1][-1][1])

    for i in range(lis_len-2,-1,-1):
        cur_len = len(dp[i])
        j = 0
        while j < cur_len and dp[i][j][0] <= level:
            temp_level, temp_val = dp[i][j]
            j += 1
        ans[i] = str(temp_val)
        if temp_level < level:
            level = temp_level

    return str(lis_len) + '\n' + ' '.join(ans)


print(sol(int(input())))
