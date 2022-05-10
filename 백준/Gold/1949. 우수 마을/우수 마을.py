import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def sol(n: int) -> int:
    def subtree_max_pop(c: int, p: int) -> tuple:
        is_c, not_c, all_not_c = popul[c], 0, 0
        chk = 1; min_gap = INF

        for cc in adjs[c]:
            if cc != p:
                is_cc, not_cc, all_not_cc = subtree_max_pop(cc, c)

                is_c += max(not_cc, all_not_cc)

                if is_cc >= not_cc:
                    chk = 0
                    not_c += is_cc
                else:
                    not_c += not_cc
                    if not_cc - is_cc < min_gap:
                        min_gap = not_cc - is_cc

                all_not_c += not_cc
        
        if chk:
            not_c -= min_gap
        
        return is_c, not_c, all_not_c
    

    INF = sys.maxsize
    map_func = lambda x: map(int, x)
    popul = [0] + list(map_func(input().split()))
    adjs = [[] for _ in range(n+1)]
    for _ in range(n-1):
        v1,v2 = map_func(input().split())
        adjs[v1].append(v2)
        adjs[v2].append(v1)

    x, y, _ = subtree_max_pop(1, 0)
    return x if x > y else y


print(sol(int(input())))
