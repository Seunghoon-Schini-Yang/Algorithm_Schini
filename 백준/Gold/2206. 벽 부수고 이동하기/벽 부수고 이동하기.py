import sys
input = sys.stdin.readline
from collections import deque

def sol(n: int, m: int) -> int:
    cnt = 0
    locs = [input().rstrip() for _ in range(n)]
    visited = [[[0,0] for _ in range(m)] for _ in range(n)]
    q = deque([(0,0,0)])

    while q:
        for _ in range(len(q)):
            i,j,flag = q.popleft()

            if i==n-1 and j==m-1:
                return cnt+1

            if flag:
                if i>0 and not visited[i-1][j][1] and locs[i-1][j]=='0':
                    q.append((i-1,j,1))
                    visited[i-1][j][1] = 1
                if i<n-1 and not visited[i+1][j][1] and locs[i+1][j]=='0':
                    q.append((i+1,j,1))
                    visited[i+1][j][1] = 1
                if j>0 and not visited[i][j-1][1] and locs[i][j-1]=='0':
                    q.append((i,j-1,1))
                    visited[i][j-1][1] = 1
                if j<m-1 and not visited[i][j+1][1] and locs[i][j+1]=='0':
                    q.append((i,j+1,1))
                    visited[i][j+1][1] = 1
            else:
                if i>0:
                    if not visited[i-1][j][0] and locs[i-1][j] =='0':
                        q.append((i-1,j,0))
                        visited[i-1][j][0] = 1
                    elif not visited[i-1][j][1] and locs[i-1][j] =='1':
                        q.append((i-1,j,1))
                        visited[i-1][j][1] = 1
                if i<n-1:
                    if not visited[i+1][j][0] and locs[i+1][j] =='0':
                        q.append((i+1,j,0))
                        visited[i+1][j][0] = 1
                    elif not visited[i+1][j][1] and locs[i+1][j] =='1':
                        q.append((i+1,j,1))
                        visited[i+1][j][1] = 1
                if j>0:
                    if not visited[i][j-1][0] and locs[i][j-1] =='0':
                        q.append((i,j-1,0))
                        visited[i][j-1][0] = 1
                    elif not visited[i][j-1][1] and locs[i][j-1] =='1':
                        q.append((i,j-1,1))
                        visited[i][j-1][1] = 1
                if j<m-1:
                    if not visited[i][j+1][0] and locs[i][j+1] =='0':
                        q.append((i,j+1,0))
                        visited[i][j+1][0] = 1
                    elif not visited[i][j+1][1] and locs[i][j+1] =='1':
                        q.append((i,j+1,1))
                        visited[i][j+1][1] = 1
        cnt += 1
    return -1


print(sol(*map(int, input().split())))
