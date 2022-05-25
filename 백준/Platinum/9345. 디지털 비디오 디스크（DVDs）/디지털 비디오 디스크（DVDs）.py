# segment tree (list)
# minmax
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(t: int) -> None:
    for _ in range(t):
        testcase(*map(int, input().split()))


def testcase(n: int, k: int) -> None:
    min_tree, max_tree = init_tree(n)

    for _ in range(k):
        q,a,b = map(int, input().split())
        if not q:
            crazy_customer(n, min_tree, max_tree, n+a, n+b)
        else:
            print(f'{is_normal(n, min_tree, max_tree, n+a, n+b+1)}\n')
    return


def init_tree(n: int) -> tuple:
    min_tree = [0]*n + [i for i in range(n)]
    max_tree = min_tree[:]
    for i in range(n-1, 0, -1):
        min_tree[i] = min(min_tree[i<<1], min_tree[i<<1|1])
        max_tree[i] = max(max_tree[i<<1], max_tree[i<<1|1])
    return min_tree, max_tree


def crazy_customer(n: int, min_tree: list, max_tree: list, a: int, b: int) -> None:
    min_tree[a], min_tree[b] = min_tree[b], min_tree[a]
    max_tree[a], max_tree[b] = max_tree[b], max_tree[a]

    while a > 1:
        min_tree[a>>1] = min(min_tree[a], min_tree[a^1])
        max_tree[a>>1] = max(max_tree[a], max_tree[a^1])
        a >>= 1

    while b > 1:
        min_tree[b>>1] = min(min_tree[b], min_tree[b^1])
        max_tree[b>>1] = max(max_tree[b], max_tree[b^1])
        b >>= 1
    return


def is_normal(n: int, min_tree: list, max_tree: list, a: int, b: int) -> str:
    miny, maxy = 100_000, 0
    av = a-n; bv = b-n-1

    while a < b:
        if a&1:
            miny = min(miny, min_tree[a])
            maxy = max(maxy, max_tree[a])
            a += 1
        if b&1:
            b ^= 1
            miny = min(miny, min_tree[b])
            maxy = max(maxy, max_tree[b])
        a >>= 1; b >>= 1

    return 'NO' if miny < av or bv < maxy else 'YES'


sol(int(input()))
