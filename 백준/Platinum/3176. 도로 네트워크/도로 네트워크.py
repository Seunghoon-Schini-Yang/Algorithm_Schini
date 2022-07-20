import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10,9))


def get_node_info(c_n: int) -> None:
    size[c_n] = 1
    for cc_n in tree[c_n]:
        if parents[c_n] != cc_n:
            parents[cc_n] = c_n
            get_node_info(cc_n)
            size[c_n] += size[cc_n]
    return


def build_chain(c_n: int, c_num: list, c_idx: int, dth: int) -> None:
    depth[c_n] = dth
    chain[c_num].append(c_n)
    chain_idx[c_n] = c_idx
    chain_num[c_n] = c_num

    max_size = max_size_node = 0
    for cc_n in tree[c_n]:
        if parents[c_n] == cc_n:
            continue
        if size[cc_n] > max_size:
            max_size_node = cc_n
            max_size = size[cc_n]

    for cc_n in tree[c_n]:
        if parents[c_n] == cc_n:
            continue
        if cc_n != max_size_node:
            build_chain(cc_n, cc_n, 0, dth+1)
        else:
            build_chain(cc_n, c_num, c_idx+1, dth)
    return


def build_segtree() -> None:
    for i in range(1, N+1):
        if len(chain[i]) >= 2:
            c_max = 0; c_min = INF
            c_len = len(chain[i])-1
            seg_max[i] = [0]*(c_len*2)

            for j in range(c_len):
                seg_max[i][j+c_len] = tree[chain[i][j]][chain[i][j+1]]
            seg_min[i] = seg_max[i][:]
            
            for j in range(c_len-1, 0, -1):
                seg_max[i][j] = max(seg_max[i][j<<1], seg_max[i][(j<<1)^1])
                seg_min[i][j] = min(seg_min[i][j<<1], seg_min[i][(j<<1)^1])
    return


def get_range_max(c_idx1: int, c_idx2: int, segtree: list) -> None:
    global miny, maxy
    while c_idx1 < c_idx2:
        if c_idx1&1:
            maxy = max(maxy, segtree[c_idx1])
            c_idx1 += 1
        if c_idx2&1:
            c_idx2 ^= 1
            maxy = max(maxy, segtree[c_idx2])
        c_idx1 >>= 1
        c_idx2 >>= 1
    return


def get_range_min(c_idx1: int, c_idx2: int, segtree: list) -> None:
    global miny, maxy
    while c_idx1 < c_idx2:
        if c_idx1&1:
            miny = min(miny, segtree[c_idx1])
            c_idx1 += 1
        if c_idx2&1:
            c_idx2 ^= 1
            miny = min(miny, segtree[c_idx2])
        c_idx1 >>= 1
        c_idx2 >>= 1
    return


def print_minmax_dist(n1: int, n2: int) -> None:
    global miny, maxy

    while chain_num[n1] != chain_num[n2]:
        if depth[n1] < depth[n2]:
            n1,n2 = n2,n1

        if seg_max[chain_num[n1]]:
            c_len = len(chain[chain_num[n1]])-1
            idx1 = c_len; idx2 = c_len+chain_idx[n1]

            get_range_max(idx1, idx2, seg_max[chain_num[n1]])
            get_range_min(idx1, idx2, seg_min[chain_num[n1]])
        
        if tree[chain_num[n1]][parents[chain_num[n1]]] > maxy:
            maxy = tree[chain_num[n1]][parents[chain_num[n1]]]
        if tree[chain_num[n1]][parents[chain_num[n1]]] < miny:
            miny = tree[chain_num[n1]][parents[chain_num[n1]]]
            
        n1 = parents[chain_num[n1]]
    
    if chain_idx[n1] - chain_idx[n2]:
        (idx1, idx2) = (chain_idx[n1], chain_idx[n2]) if chain_idx[n1] < chain_idx[n2] else (chain_idx[n2], chain_idx[n1])
        c_len = len(chain[chain_num[n1]])-1
        idx1 += c_len; idx2 += c_len

        get_range_max(idx1, idx2, seg_max[chain_num[n1]])
        get_range_min(idx1, idx2, seg_min[chain_num[n1]])

    print(miny, maxy)
    return


if __name__ == '__main__':
    N = int(input())
    INF = sys.maxsize
    tree = [{} for _ in range(N+1)]
    size = [0]*(N+1)
    parents = [0]*(N+1)
    depth = [0]*(N+1)
    chain = [[] for _ in range(N+1)]
    chain_idx = [0]*(N+1) 
    chain_num = [0]*(N+1)

    for _ in range(N-1):
        A,B,C = map(int, input().split())
        tree[A][B] = C
        tree[B][A] = C

    get_node_info(1)
    build_chain(1, 1, 0, 0)

    seg_max = [[] for _ in range(N+1)]
    seg_min = [[] for _ in range(N+1)]

    build_segtree()

    miny = INF; maxy = 0
    for _ in range(int(input())):
        print_minmax_dist(*map(int, input().split()))
        miny = INF; maxy = 0
