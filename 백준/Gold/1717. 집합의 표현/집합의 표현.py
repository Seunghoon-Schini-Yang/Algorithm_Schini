# my
# audrjs3232 님 코드 참고
# rank list 안 만들고, rank를 parent 음수 절대값 크기로 표현
# disjoint set + path compression + recursive + union by rank
import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    def find(x: int) -> int:
        if parent[x] < 0:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    
    def union(x: int, y: int):
        if parent[x] > parent[y]:
            parent[x] = y
        else:
            parent[y] = x
            if parent[x] == parent[y]:
                parent[x] -= 1

    
    parent = [-1] * (n+1)
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
