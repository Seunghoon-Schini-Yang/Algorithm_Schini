# dp + recursive
import sys
input = sys.stdin.readline
sys.setrecursionlimit(pow(10, 9))


def sol(n: int, r: int, q: int) -> str:
    def make_tree(v: int, p: int):
        c_sum = 0
        for c_v in tree[v]:
            if c_v != p:
                c_sum += (make_tree(c_v, v) + 1)

        subtree_dp[v] = c_sum+1
        return c_sum

    
    tree = [[] for _ in range(n+1)]
    subtree_dp = [0] * (n+1)
    for _ in range(n-1):
        v1,v2 = map(int, input().split())
        tree[v1].append(v2)
        tree[v2].append(v1)
    
    make_tree(r, -1)
    return '\n'.join(str(subtree_dp[int(input())]) for _ in range(q))


print(sol(*map(int, input().split())))
