from collections import deque


def sol(f: int, s: int, g: int, u: int, d: int) -> int or str:
    visited = [-1]*(f+1)
    visited[s] = 0
    que = deque([s])
    while que:
        cur_floor = que.popleft()
        if cur_floor == g:
            return visited[cur_floor]
        
        up_floor = cur_floor+u
        if up_floor <= f and visited[up_floor] == -1:
            visited[up_floor] = visited[cur_floor]+1
            que.append(up_floor)

        down_floor = cur_floor-d
        if 0 < down_floor and visited[down_floor] == -1:
            visited[down_floor] = visited[cur_floor]+1
            que.append(down_floor)

    return 'use the stairs'


print(sol(*map(int, input().split())))
