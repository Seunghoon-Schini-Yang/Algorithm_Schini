import sys
input = sys.stdin.readline
sys.setrecursionlimit(20_000)


def sol(t: int) -> None:
    def case(n: int) -> int:
        def depth_dfs(node: int, depth: int) -> None:
            depths[node] = depth
            for v in children[node]:
                depth_dfs(v, depth+1)
            return


        def nca(v1: int, v2: int) -> int:
            if depths[v1] > depths[v2]:
                v1,v2 = v2,v1
            while depths[v1] != depths[v2]:
                v2 = parents[v2]
            while v1 != v2:
                v1 = parents[v1]
                v2 = parents[v2]
            return v1

        
        parents = [0]*(n+1)
        children = [[] for _ in range(n+1)]
        for _ in range(n-1):
            p,c = map(int, input().split())
            parents[c] = p
            children[p].append(c)

        for i in range(1, n+1):
            if not parents[i]:
                root = i
                break
        
        depths = [0]*(n+1)
        depth_dfs(root, 0)
        return nca(*map(int, input().split()))


    return '\n'.join(map(str, [case(int(input())) for _ in range(t)]))


print(sol(int(input())))
