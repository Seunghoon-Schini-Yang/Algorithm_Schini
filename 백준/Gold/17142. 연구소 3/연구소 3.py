import sys
input = sys.stdin.readline
from copy import deepcopy as dcp
from itertools import combinations as comb


def adjs(r: int, c: int) -> tuple:
    yield r+1, c
    yield r-1, c
    yield r, c+1
    yield r, c-1


def bfs(que: list) -> None:
    global miny

    visited = dcp(lab)
    for r,c in que:
        visited[r][c] = 1

    elapsed = 0
    while True:
        if miny <= elapsed:
            return
        
        temp = list()
        for _ in range(len(que)):
            for nr,nc in adjs(*que.pop()):
                if 0<=nr<n and 0<=nc<n and visited[nr][nc] != 1:
                    visited[nr][nc] = 1
                    temp.append((nr,nc))

        if not temp:
            break
        is_break = True
        for r,c in temp:
            if (r,c) not in virus:
                is_break = False
                break
        if is_break and min(map(min, visited)):
            break

        que = temp
        elapsed += 1

    if not min(map(min, visited)):
        return
    miny = elapsed
    return


if __name__ == '__main__':
    n,m = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(n)]

    virus = set()
    for r in range(n):
        for c in range(n):
            if lab[r][c] == 2:
                virus.add((r,c))
    
    miny = 10000
    for pair in comb(virus, m):
        bfs(list(pair))
    print(-1 if miny==10000 else miny)
