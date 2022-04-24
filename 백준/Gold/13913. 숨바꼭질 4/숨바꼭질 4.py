import sys
input = sys.stdin.readline
from collections import deque, defaultdict

def sol(s: int, e: int) -> str:
    path_dp = dict()
    cnt, maxy = 0, sys.maxsize
    q = deque([(-1,s)])
    while q:
        for _ in range(len(q)):
            if not maxy:
                path = [str(i) for i in range(e,max_idx+1)]
                while max_idx != s:
                    max_idx = path_dp[max_idx]
                    path.append(str(max_idx))
                return str(cnt) + '\n' + ' '.join(reversed(path))

            pre,cur = q.popleft()
            gap = cur - e
            if not gap:
                path = [str(cur)]
                while cur != s:
                    cur = path_dp[cur]
                    path.append(str(cur))
                return str(cnt) + '\n' + ' '.join(reversed(path))
            elif 0 < gap < maxy:
                maxy = gap
                path_dp[cur] = pre
                max_idx = cur
            elif gap >= maxy:
                continue
            else:
                if cur > s//2 and path_dp.get(cur-1,-1) == -1:
                    q.append((cur,cur-1))
                    path_dp[cur-1] = cur
                if path_dp.get(cur+1,-1) == -1:
                    q.append((cur,cur+1))
                    path_dp[cur+1] = cur
                if cur*2-e < maxy and path_dp.get(cur*2,-1) == -1:
                    q.append((cur,cur*2))
                    path_dp[cur*2] = cur

        maxy -= 1
        cnt += 1
    
    path = [str(i) for i in range(e,max_idx+1)]
    while max_idx != s:
        max_idx = path_dp[max_idx]
        path.append(str(max_idx))
    return str(maxy+cnt) + '\n' + ' '.join(reversed(path))


print(sol(*map(int, input().split())))
