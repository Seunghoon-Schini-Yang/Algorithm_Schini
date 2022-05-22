import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int, m: int, k: int) -> str:
    arr = [int(input()) for _ in range(n)]
    bitree = make_tree(n, arr)

    for _ in range(m+k):
        a,b,c = map(int, input().split())
        if a == 1:
            arr[b-1], c = c, c-arr[b-1]
            update_tree(n, bitree, b, c)
        else:
            print(f'{partial_sum(bitree, b, c)}\n')
    return


def make_tree(n: int, arr: list) -> list:
    bitree = [0] * (n+1)
    for i,j in enumerate(range(1, n+1)):
        k = j
        while k <= n:
            bitree[k] += arr[i]
            k += k&-k
    return bitree


def update_tree(n: int, tree: list, idx: int, val: int) -> None:
    while idx <= n:
        tree[idx] += val
        idx += idx&-idx
    return


def partial_sum(tree: list, s: int, e: int) -> int:
    return range_sum(tree, e) - range_sum(tree, s-1)


def range_sum(tree: list, idx: int) -> int:
    p_sum = 0
    while idx:
        p_sum += tree[idx]
        idx -= idx&-idx
    return p_sum


sol(*map(int, input().split()))
