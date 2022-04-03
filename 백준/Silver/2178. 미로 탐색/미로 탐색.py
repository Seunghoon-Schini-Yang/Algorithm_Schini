import sys
input = sys.stdin.readline
from collections import deque

def sol(n: int, m: int) -> int:
    mazes = [list(map(int, input().rstrip())) for _ in range(n)]
    queue = deque([(0, 0)])
    left = 1
    ans = 0
    
    while queue:
        i, j = queue.popleft()
        if i == n-1 and j == m-1:
            ans += 1
            break
        left -= 1

        if mazes[i][j]:
            mazes[i][j] = 0
            if i > 0:
                queue.append((i-1, j))
            if i < n-1:
                queue.append((i+1, j))
            if j > 0:
                queue.append((i, j-1))
            if j < m-1:
                queue.append((i, j+1))
        
        if not left:
            ans += 1
            left = len(queue)

    return ans


print(sol(*map(int, input().split())))
