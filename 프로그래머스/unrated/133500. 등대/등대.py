import sys
sys.setrecursionlimit(pow(10, 9))


def solution(n, lighthouse):
    def dfs(parent, node):   
        _on = _off = 0
        for child in graph[node]:
            if child == parent:  # skip parent node
                continue
            dfs(node, child)  # search & update child node
            _on += min(memo[child])  # if current light is "on", add "min" value from child
            _off += memo[child][0]  # if cur "off", then add "on" value from child
        memo[node] = [_on+1, _off]  # update current node
    
    
    # init graph
    graph = [[] for _ in range(n+1)]
    for n1, n2 in lighthouse:
        graph[n1].append(n2)
        graph[n2].append(n1)
    # init memo
    memo = [[0, 0] for _ in range(n+1)]
    # run dfs
    dfs(0, 1)
    # return answer
    return min(memo[1])
