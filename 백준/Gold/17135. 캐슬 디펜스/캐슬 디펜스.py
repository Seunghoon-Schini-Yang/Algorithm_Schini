import sys
input = sys.stdin.readline
from itertools import combinations as comb
from copy import deepcopy
from collections import deque


def adjs(r: int, c: int) -> tuple:
    yield r, c-1
    yield r-1, c
    yield r, c+1


def bfs(field: list, r: int, c: int) -> tuple:
    if field[r][c]:
        return r, c
    visited = [[False]*M for _ in range(N)]
    visited[r][c] = True

    que = deque([(r,c)])
    for _ in range(D-1):
        for _ in range(len(que)):
            for nr,nc in adjs(*que.popleft()):
                if 0<=nr<N and 0<=nc<M and not visited[nr][nc]:
                    if field[nr][nc]:
                        return nr, nc
                    visited[nr][nc] = True
                    que.append((nr,nc))
        if not que:
            return False
    return False


def calc_case(case: tuple) -> int:
    case_field = deepcopy(field)
    case_kill = 0
    
    for r in range(N-1, -1, -1):
        enemy_spot = set()
        for i in range(3):
            is_target = bfs(case_field, r, case[i])
            if is_target:
                enemy_spot.add(is_target)
        case_kill += len(enemy_spot)
        for rr,cc in enemy_spot:
            case_field[rr][cc] = 0
    return case_kill


if __name__ == '__main__':
    N,M,D = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(N)]
    print(max(calc_case(case) for case in comb(range(M), 3)))
