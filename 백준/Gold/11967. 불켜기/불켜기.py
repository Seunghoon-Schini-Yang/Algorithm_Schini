import sys
input = sys.stdin.readline
from collections import defaultdict


if __name__ == '__main__':
    N, M = map(int, input().split())
    swtch = defaultdict(set)
    for _ in range(M):
        x, y, xx, yy = map(lambda x: int(x)-1, input().split())
        swtch[(x,y)].add((xx, yy))
    
    cnt = 1
    memo = [[0] * N for _ in range(N)]
    memo[0][0] = 3
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    q = [(0,0)]
    while q:
        tmp = []
        for x, y in q:
            for xx, yy in zip(dx, dy):
                xxx, yyy = x+xx, y+yy
                if not (0 <= xxx < N and 0 <= yyy < N) or memo[xxx][yyy] in (1, 3):
                    continue
                if memo[xxx][yyy] == 2:
                    tmp.append((xxx, yyy))
                    memo[xxx][yyy] = 3
                else:
                    memo[xxx][yyy] = 1
            for xx, yy in swtch[(x,y)]:
                if memo[xx][yy] in (2, 3):
                    continue
                cnt += 1
                if memo[xx][yy] == 1:
                    tmp.append((xx, yy))
                    memo[xx][yy] = 3
                else:
                    memo[xx][yy] = 2
        q = tmp
    print(cnt)
