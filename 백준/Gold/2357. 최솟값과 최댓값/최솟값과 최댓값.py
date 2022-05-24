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
        partial_minmax(tree_max, tree_min, n+a-1, n+b)
    return


def partial_minmax(tree_max: list, tree_min: list, s: int, e: int) -> None:
    maxy = 1; miny = 1_000_000_000
    while s < e:
        if s&1:
            maxy = max(maxy, tree_max[s])
            miny = min(miny, tree_min[s])
            s += 1
        if e&1:
            e ^= 1
            maxy = max(maxy, tree_max[e])
            miny = min(miny, tree_min[e])
        s >>= 1; e >>= 1
    print(f'{miny} {maxy}\n')
    return


sol(*map(int, input().split()))
