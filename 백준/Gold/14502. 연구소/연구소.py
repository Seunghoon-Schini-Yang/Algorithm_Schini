from itertools import combinations as comb
from copy import deepcopy


if __name__ == '__main__':
    maxy = 0
    N, M = map(int, input().split())
    lab = [list(map(int, input().split())) for _ in range(N)]
    es, vs = [], []
    for r in range(N):
        for c in range(M):
            if lab[r][c] == 2:
                vs.append((r, c))
            elif not lab[r][c]:
                es.append((r, c))
    ini = len(es)-3
    
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    
    for walls in comb(es, 3):
        curlab = deepcopy(lab)
        for w in walls:
            curlab[w[0]][w[1]] = 1
        cur = ini
        stack = vs[:]
        while stack:
            pr, pc = stack.pop()
            for i in range(4):
                cr, cc = pr+dr[i], pc+dc[i]
                if 0 <= cr < N and 0 <= cc < M and not curlab[cr][cc]:
                    curlab[cr][cc] = 2
                    cur -= 1
                    stack.append((cr, cc))
        maxy = max(maxy, cur)
    print(maxy)
