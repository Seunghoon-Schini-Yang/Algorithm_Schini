# my
# disjoint set
import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    def find(x: int) -> int:
        temp = []
        while x != root[x]:
            temp.append(x)
            x = root[x]
        
        # path compression
        for v in temp:
            root[v] = x
        
        return x

    
    root = [i for i in range(n+1)]
    ans = list()
    for _ in range(m):
        op,a,b = map(int, input().split())
        x,y = find(a),find(b)
        if op:
            if x == y:
                ans.append('YES')
            else:
                ans.append('NO')
        else:
            if x == y:
                continue
            else:
                root[y] = x

    return '\n'.join(ans)


print(sol(*map(int, input().split())))
