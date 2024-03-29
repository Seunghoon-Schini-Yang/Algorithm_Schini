# disjoint set
# without defaultdict + less memory
import sys
input = sys.stdin.readline

def sol(f: int) -> str:
    def find(x: str) -> str:
        if isinstance(ps.get(x, -1), int):
            if ps.get(x, 1) == 1:
                ps[x] = 1
            return x
        ps[x] = find(ps[x])
        return ps[x]


    def union(x: str, y: str) -> str:
        x_r,y_r = find(x),find(y)
        if x_r == y_r:
            return str(ps[x_r])
            
        cur = ps[x_r] + ps[y_r]
        if ps[x_r] > ps[y_r]:
            ps[y_r] = x_r
            ps[x_r] = cur
        else:
            ps[x_r] = y_r
            ps[y_r] = cur
        
        return str(cur)

        
    ps = dict()

    res = [0]*f
    for i in range(f):
        f1,f2 = map(str, input().split())
        res[i] = union(f1, f2)

    return '\n'.join(res)


print('\n'.join(sol(int(input())) for _ in range(int(input()))))
