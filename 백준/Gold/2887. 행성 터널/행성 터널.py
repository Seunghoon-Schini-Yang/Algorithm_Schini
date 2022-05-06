import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    def find(v: int) -> int:
        if rs[v] < 0:
            return v
        rs[v] = find(rs[v])
        return rs[v]


    def union(w: int, v1: int, v2: int) -> int:
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

    
    rs = [-1] * n
    locs = [0] * n
    edges = [0] * (3*(n-1))
    k = 0

    for i in range(n):
        locs[i] = (*map(int, input().split()), i)

    xyz = zip(sorted(locs), sorted(locs, key=lambda x: x[1]), sorted(locs, key=lambda x: x[2]))
    (pxw,_,_,pxn), (_,pyw,_,pyn), (_,_,pzw,pzn) = next(xyz)

    for _ in range(n-1):
        (cxw,_,_,cxn), (_,cyw,_,cyn), (_,_,czw,czn) = next(xyz)
        edges[k] = (abs(cxw-pxw), pxn, cxn)
        k += 1
        edges[k] = (abs(cyw-pyw), pyn, cyn)
        k += 1
        edges[k] = (abs(czw-pzw), pzn, czn)
        k += 1
        pxw,pxn,pyw,pyn,pzw,pzn = cxw,cxn,cyw,cyn,czw,czn
    edges.sort()

    return sum(union(w,v1,v2) for w,v1,v2 in edges)


print(sol(int(input())))
