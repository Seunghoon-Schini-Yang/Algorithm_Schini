import sys
input = sys.stdin.readline
from collections import deque

def sol(w: int, h: int) -> int:
    ans = cnt = 0
    qs = list()
    tomatoes = [[-1] * (w+2)]
    for i in range(1, h+1):
        tomatoes.append([-1] + list(map(int, input().split())) + [-1])
        for j in range(1, w+1):
            if not tomatoes[i][j]:
                cnt += 1
            if tomatoes[i][j] == 1:
                qs.append(deque([(i,j)]))
    tomatoes.append([-1] * (w+2))

    break_chk = 1
    while break_chk:
        break_chk = 0
        for q in qs:
            temp = deque()
            while q:
                i, j = q.popleft()
                for x, y in ((i+1,j), (i-1,j), (i,j+1), (i,j-1)):
                    if not tomatoes[x][y]:
                        tomatoes[x][y] = 1
                        cnt -= 1
                        temp.append((x,y))
                        break_chk = 1
            q.extend(temp)
        ans += break_chk

    return ans if not cnt else -1


print(sol(*map(int, input().split())))
