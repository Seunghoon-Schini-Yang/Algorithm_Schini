import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def is_bipartite(v, e):
    def dfs(v, b):
        memo[v] = b
        for cv in graph[v]:
            if memo[cv] == b^1:
                continue
            if memo[cv] == b or not dfs(cv, b^1):
                return False
        return True
    
    
    memo = [-1] * (v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    answer = all(dfs(i, 0) for i in range(1, v+1) if memo[i] == -1)
    return 'YES' if answer else 'NO'


if __name__ == '__main__':
    print('\n'.join(is_bipartite(*map(int, input().split())) for _ in range(int(input()))))
    