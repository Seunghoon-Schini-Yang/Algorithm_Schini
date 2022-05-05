import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def find(v: int) -> int:
        if rs[v] < 0:
            return v
        rs[v] = find(rs[v])
        return rs[v]


    def union(v1: int, v2: int, w: float) -> float:
        r1,r2 = find(v1),find(v2)
        if r1 == r2:
            return 0.0

        if rs[r1] < rs[r2]:
            rs[r2] = r1
        else:
            if rs[r1] == rs[r2]:
                rs[r2] -= 1
            rs[r1] = r2
        return w

    
    rs = [-1] * n
    locs = [0] * n
    edges = [0] * (n*(n-1)//2)
    k = 0
    for i in range(n):
        locs[i] = tuple(map(float, input().split()))
        for j in range(i):
            edges[k] = (i, j, pow(pow(locs[i][0] - locs[j][0], 2) + pow(locs[i][1] - locs[j][1], 2), 0.5))
            k += 1
    edges.sort(key=lambda x: x[2])

    return round(sum(union(a,b,w) for a,b,w in edges), 2)


print(sol(int(input())))
