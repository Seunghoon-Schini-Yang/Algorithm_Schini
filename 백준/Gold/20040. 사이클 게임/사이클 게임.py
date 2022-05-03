# my
# disjoint set
import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> int:
    def find(x: int) -> int:
        if ps[x] < 0:
            return x
        ps[x] = find(ps[x])
        return ps[x]
    

    def union(x: int, y: int) -> bool:
        x_r,y_r = find(x),find(y)
        if x_r == y_r:
            return True

        if ps[x_r] > ps[y_r]:
            ps[x_r] = y_r
        else:
            if ps[x_r] == ps[y_r]:
                ps[x_r] -= 1
            ps[y_r] = x_r
        
        return False


    ps = [-1]*n
    for i in range(1, m+1):
        a,b = map(int, input().split())
        if union(a,b):
            return i
    return 0


print(sol(*map(int, input().split())))
