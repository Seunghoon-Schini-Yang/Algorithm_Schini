import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))
from math import log2, ceil


def get_odr(p_node: int, node: int, depth: int) -> None:
    global pre_odr, post_odr

    pre_odr += 1
    pre_o[node] = pre_odr
    depths[node] = depth
    parents[node] = p_node

    for c_n in tree[node]:
        if c_n != p_node:
            get_odr(node, c_n, depth+1)
    
    post_odr += 1
    post_o[node] = post_odr
    return


def is_ancestor(n1: int, n2: int) -> bool:
    if pre_o[n1] < pre_o[n2] and post_o[n1] > post_o[n2]:
        return True
    return False


def get_lca(n1: int, n2: int) -> int:
    if n1 == n2:
        return n1
    if depths[n1] > depths[n2]:
        n1,n2 = n2,n1
    if is_ancestor(n1, n2):
        return n1 if depths[n1] < depths[n2] else n2

    lo = n1; hi = sparse[logN-1][n1]
    for i in range(logN-2, -1, -1):
        mid = sparse[i][lo]
        if is_ancestor(mid, n2):
            hi = mid
        else:
            lo = mid
    return hi


if __name__ == '__main__':

    # init
    N = int(input())
    tree = [[] for _ in range(N+1)]
    pre_o = [0]*(N+1)
    post_o = [0]*(N+1)
    parents = [0]*(N+1)
    depths = [0]*(N+1)
    pre_odr = post_odr = 0

    # get_tree
    for _ in range(N-1):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    # get pre, post odr & depth
    get_odr(0, 1, 1)

    # get sparse table
    logN = ceil(log2(max(depths)-1))+1
    sparse = [[0]*(N+1) for _ in range(logN)]
    sparse[0] = parents
    sparse[0][1] = 1

    for i in range(logN-1):
        for node in range(1, N+1):
            sparse[i+1][node] = sparse[i][sparse[i][node]]

    # get lca
    print('\n'.join(map(str, [get_lca(*map(int, input().split())) for _ in range(int(input()))])))
