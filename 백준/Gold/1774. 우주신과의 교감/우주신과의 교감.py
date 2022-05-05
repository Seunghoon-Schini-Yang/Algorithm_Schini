import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> float:
    def find(v: int) -> int:
        if rs[v] < 0:
            return v
        rs[v] = find(rs[v])
        return rs[v]

    
    def union(w: float, v1: int, v2: int) -> float:
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


    locs = [0] * (n+1)
    rs = [-1] * (n+1)
    edges = [0] * (n*(n-1)//2)
    k = 0
    
    for i in range(1, n+1):
        locs[i] = tuple(map(float, input().split()))
        for j in range(1, i):
            edges[k] = (pow(pow(locs[i][0]-locs[j][0], 2)+pow(locs[i][1]-locs[j][1], 2), 0.5), j,i)
            k += 1
    
    for _ in range(m):
        union(0.0, *map(int, input().split()))

    edges.sort()
    ans = str(round(sum(union(w,v1,v2) for w,v1,v2 in edges), 2))
    return ans+'0' if ans[-2]=='.' else ans


print(sol(*map(int, input().split())))
