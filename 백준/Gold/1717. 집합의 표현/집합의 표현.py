# my
# disjoint set + path compression + recursive + union by rank
import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    def find(x: int) -> int:
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    
    def union(x: int, y: int):
        if rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rank[x] == rank[y]:
                rank[y] += 1

    
    rank = [0] * (n+1)
    parent = [i for i in range(n+1)]
    ans = list()
    for _ in range(m):
        op,a,b = map(int, input().split())
        x,y = find(a),find(b)
        if op:
            ans.append('YES' if x==y else 'NO')
        else:
            if x != y:
                union(x, y)
    
    return '\n'.join(ans)


print(sol(*map(int, input().split())))
