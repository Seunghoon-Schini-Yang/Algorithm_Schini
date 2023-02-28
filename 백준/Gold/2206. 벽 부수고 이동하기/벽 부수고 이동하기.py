import sys
input = sys.stdin.readline
from collections import deque


def sol(n: int, m: int) -> int:
    def adjs(i: int, j: int) -> tuple:
        if i > 0:  yield i-1, j
        if j > 0:  yield i, j-1
        if i < n-1:  yield i+1, j
        if j < m-1:  yield i, j+1

    
    cnt = 1
    locs = [input().rstrip() for _ in range(n)]
    is_visited = [[[False, False] for _ in range(m)] for _ in range(n)]
    is_visited[0][0] = [True, True]
    q = deque([(0,0,0)])

    while q:
        for _ in range(len(q)):
            r,c,flag = q.popleft()

            if r==n-1 and c==m-1:
                return cnt

            for i, j in adjs(r, c):
                if flag:
                    if is_visited[i][j][1]:
                        continue
                    if locs[i][j] == '0':
                        is_visited[i][j][1] = True
                        q.append((i,j,1))
                else:
                    if is_visited[i][j][0]:
                        continue
                    is_visited[i][j][0] = True
                    q.append((i,j,0)) if locs[i][j] == '0' else q.append((i,j,1))
        cnt += 1
    return -1


print(sol(*map(int, input().split())))

