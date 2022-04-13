# my
# floyd warshall
# if 출발 노드 = 도착 노드, 초기값 INF로 설정
import sys
input = sys.stdin.readline
import math

def sol(v: int, e: int) -> int:
    INF = math.inf
    floyd = [[INF]*(v+1) for _ in range(v+1)]
    for _ in range(e):
        a,b,c = map(int, input().split())
        floyd[a][b] = c

    for mid in range(1,v+1):
        for start in range(1,v+1):
            if start==mid:
                continue
            for end in range(1,v+1):
                if mid==end:
                    continue
                if floyd[start][mid] + floyd[mid][end] < floyd[start][end]:
                    floyd[start][end] = floyd[start][mid] + floyd[mid][end]

    ans = min(floyd[i][i] for i in range(1,v+1))
    return -1 if math.isinf(ans) else ans


print(sol(*map(int, input().split())))
