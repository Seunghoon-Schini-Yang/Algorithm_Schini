# binary search + dynamic programming
# redpigeon 님 코드 참고
import sys
input = sys.stdin.readline
from bisect import bisect_left

def sol(n: int) -> str:
    seq = list(map(int, input().split()))
    track = [0]*n
    lis = [seq[0]]
    lis_len = 1

    for i in range(1,n):
        v = seq[i]
        if v > lis[-1]:
            lis.append(v)
            track[i] = lis_len
            lis_len += 1
        else:
            cur_idx = bisect_left(lis,v)
            lis[cur_idx] = v
            track[i] = cur_idx

    print(lis_len)

    path = [0]*lis_len
    lis_len -= 1
    for i in range(n-1,-1,-1):
        if lis_len < 0:
            break
        if track[i] == lis_len:
            path[lis_len] = seq[i]
            lis_len -= 1

    print(*path)


sol(int(input()))
