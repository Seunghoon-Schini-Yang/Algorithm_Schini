import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))
from math import log2, ceil


def get_odr(p_node: int, node: int, depth: int) -> None:
    depths[node] = depth
    parents[node] = p_node
    for c_n in tree[node]:
        if c_n != p_node:
            get_odr(node, c_n, depth+1)
    return


def get_lca(n1: int, n2: int) -> int:
    if n1 == n2:
        return n1
    if depths[n1] < depths[n2]:
        n1,n2 = n2,n1

    gap = depths[n1]-depths[n2]
    for i in range(logN):
        if gap&(1<<i):
            n1 = sparse[i][n1]

    if n1 == n2:
        return n1
    
    for i in range(logN-1, -1, -1):
        if sparse[i][n1] != sparse[i][n2]:
            n1 = sparse[i][n1]
            n2 = sparse[i][n2]
    return sparse[0][n1]


if __name__ == '__main__':
    # init
    N = int(input())
    tree = [[] for _ in range(N+1)]
    parents = [0]*(N+1)
    depths = [0]*(N+1)

    # get_tree
    for _ in range(N-1):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # get parents & depth
    get_odr(0, 1, 0)

    # get sparse table
    logN = ceil(log2(max(depths)))+1
    sparse = [[0]*(N+1) for _ in range(logN)]
    sparse[0] = parents
    sparse[0][1] = 1

    for i in range(logN-1):
        for node in range(1, N+1):
            sparse[i+1][node] = sparse[i][sparse[i][node]]

    # get lca
    print('\n'.join(map(str, [get_lca(*map(int, input().split())) for _ in range(int(input()))])))
