import sys
input = sys.stdin.readline
from collections import deque

def sol(b: int, w: int, h: int) -> int:
    ans = cnt = 0
    queue = deque()
    tomatoes = [[[-1]*(b+2) for _ in range(w+2)]]
    for i in range(1, h+1):
        temp = [[-1]*(b+2)]
        for j in range(1, w+1):
            temp.append([-1]+[*map(int, input().split())]+[-1])
            for k in range(1, b+1):
                if not temp[j][k]:
                    cnt += 1
                elif temp[j][k] == 1:
                    queue.append((i,j,k))
        temp.append([-1]*(b+2))
        tomatoes.append(temp)
    tomatoes.append([[-1]*(b+2) for _ in range(w+2)])
    
    while queue:
        for _ in range(len(queue)):
            i, j, k = queue.pop()
            for x, y, z in ((i+1,j,k),(i-1,j,k),(i,j+1,k),(i,j-1,k),(i,j,k+1),(i,j,k-1)):
                if not tomatoes[x][y][z]:
                    tomatoes[x][y][z] = 1
                    cnt -= 1
                    queue.appendleft((x,y,z))
        ans += 1

    return ans-1 if not cnt else -1


print(sol(*map(int, input().split())))
