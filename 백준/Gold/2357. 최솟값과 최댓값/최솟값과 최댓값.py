# segment tree (list)
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int, m: int) -> None:
    tree_max = [0] * (2*n)
    tree_max[n:] = [int(input()) for _ in range(n)]
    tree_min = tree_max[:]

    for i in range(n-1, 0, -1):
        tree_max[i] = max(tree_max[i<<1], tree_max[i<<1|1])
        tree_min[i] = min(tree_min[i<<1], tree_min[i<<1|1])

    for _ in range(m):
        a,b = map(int, input().split())
        print(f'{partial_minmax(tree_min, n+a-1, n+b, False)} {partial_minmax(tree_max, n+a-1, n+b, True)}\n')
    return


def partial_minmax(tree, s: int, e: int, is_max: bool) -> int:
    f = max if is_max else min
    res = 1 if is_max else 1_000_000_000
    while s < e:
        if s&1:
            res = f(res, tree[s])
            s += 1
        if e&1:
            e ^= 1
            res = f(res, tree[e])
        s >>= 1; e >>= 1
    return res


sol(*map(int, input().split()))
