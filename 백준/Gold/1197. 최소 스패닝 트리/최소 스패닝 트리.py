# my : (python3)
# mst (kruskal)
import sys
input = sys.stdin.readline


def sol(v: int, e: int) -> int:
    def find(v: int) -> int:
        if rs[v] < 0:
            return v
        rs[v] = find(rs[v])
        return rs[v]


    def union(v1: int, v2: int, w: int) -> int:
        r1,r2 = find(v1),find(v2)
        if r1 == r2:
            return 0
        
        if rs[r1] < rs[r2]:
            rs[r2] = r1
        else:
            if rs[r1] == rs[r2]:
                rs[r2] -= 1
            rs[r1] = r2
        return w


    rs = [-1] * (v+1)
    edges = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])

    return sum(union(a,b,w) for a,b,w in edges)


print(sol(*map(int, input().split())))
