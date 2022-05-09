# my
# dp + recursive
import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def sol(n: int) -> int:
    def get_subtree_min(c: int, p: int) -> tuple:
        is_c, not_c = 1, 0
        for cc in adjs[c]:
            if cc != p:
                is_cc, not_cc = get_subtree_min(cc, c)
                is_c += min(is_cc, not_cc)
                not_c += is_cc

        return is_c, not_c


    adjs = [[] for _ in range(n+1)]
    for _ in range(n-1):
        v1,v2 = map(int, input().split())
        adjs[v1].append(v2)
        adjs[v2].append(v1)
    
    return min(get_subtree_min(1, 0))


print(sol(int(input())))
