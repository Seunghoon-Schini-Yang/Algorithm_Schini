import sys
input = sys.stdin.readline
from collections import deque

def sol(n: int) -> str:
    return '\n'.join(str(knigt_moves(int(input()))) for _ in range(n))


def knigt_moves(l: int) -> int:
    cnt = 0
    s_i, s_j = map(int, input().split())
    e_i, e_j = map(int, input().split())
    visited = [[1]*(l) for _ in range(l)]
    visited[s_i][s_j] = 0
    q = deque([(s_i, s_j)])

    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            if i==e_i and j==e_j:
                return cnt
            if i>0:
                if j>1 and visited[i-1][j-2]:
                    q.append((i-1,j-2))
                    visited[i-1][j-2] = 0
                if j<l-2 and visited[i-1][j+2]:
                    q.append((i-1,j+2))
                    visited[i-1][j+2] = 0
            if i>1:
                if j>0 and visited[i-2][j-1]:
                    q.append((i-2,j-1))
                    visited[i-2][j-1] = 0
                if j<l-1 and visited[i-2][j+1]:
                    q.append((i-2,j+1))
                    visited[i-2][j+1] = 0
            if i<l-1:
                if j>1 and visited[i+1][j-2]:
                    q.append((i+1,j-2))
                    visited[i+1][j-2] = 0
                if j<l-2 and visited[i+1][j+2]:
                    q.append((i+1,j+2))
                    visited[i+1][j+2] = 0
            if i<l-2:
                if j>0 and visited[i+2][j-1]:
                    q.append((i+2,j-1))
                    visited[i+2][j-1] = 0
                if j<l-1 and visited[i+2][j+1]:
                    q.append((i+2,j+1))
                    visited[i+2][j+1] = 0
        cnt += 1


print(sol(int(input())))
