# binary indexed tree (fenwick tree)
import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> str:
    bitree = make_tree(n, list(map(int, input().split())))
    return '\n'.join(map(str, [partial_sum(bitree, *map(int, input().split())) for _ in range(m)]))


def make_tree(n: int, arr: list) -> list:
    bitree = [0] * (n+1)
    for i,j in enumerate(range(1, n+1)):
        k = j
        while k <= n:
            bitree[k] += arr[i]
            k +=  k&-k
    return bitree


def partial_sum(tree: list, s: int, e: int) -> int:
    return range_sum(tree, e) - range_sum(tree, s-1)


def range_sum(tree: list, idx: int) -> int:
    p_sum = 0
    while idx:
        p_sum += tree[idx]
        idx -= idx&-idx
    return p_sum


print(sol(*map(int, input().split())))
