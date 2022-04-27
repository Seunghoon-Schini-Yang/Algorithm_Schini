# my
# dfs + recursive
import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))

def sol(n: int) -> int:
    def dfs(v: int, p_v: int):
        maxy = maxy_v = 0
        if v != p_v and len(tree[v]) == 1:
            return v, 0
        
        for key,val in tree[v].items():
            if key != p_v:
                leaf, acc = dfs(key, v)
                if acc+val > maxy:
                    maxy = acc+val
                    maxy_v = leaf

        return maxy_v, maxy


    tree = [{} for _ in range(n+1)]
    for _ in range(n-1):
        a,b,c = map(int, input().split())
        tree[a][b] = c
        tree[b][a] = c
    
    v1 = dfs(1, 1)[0]
    return dfs(v1, v1)[1]


print(sol(int(input())))
