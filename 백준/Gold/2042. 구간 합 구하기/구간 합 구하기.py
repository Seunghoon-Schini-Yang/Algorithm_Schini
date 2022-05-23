# segment tree (list)
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int, m: int, k: int) -> None:
    tree = [0] * (2*n + 1)
    tree[n+1:] = [int(input()) for _ in range(n)]
    for i in range(2*n, 1, -1):
        tree[i>>1] += tree[i]

    for _ in range(m+k):
        a,b,c = map(int, input().split())
        if a&1:
            update_tree(tree, b+n, c)
        else:
            print(f'{partial_sum(tree, b+n, c+n)}\n')
    return


def update_tree(tree: list, idx: int, val: int) -> None:
    val -= tree[idx]
    while idx:
        tree[idx] += val
        idx >>= 1
    return


def partial_sum(tree: list, s: int, e: int) -> int:
    p_sum = 0
    while s < e:
        if s&1:
            p_sum += tree[s]
            s += 1
        if not e&1:
            p_sum += tree[e]
            e -= 1
        if s < e:
            s >>= 1; e >>= 1
    if s == e:
        p_sum += tree[s]
    return p_sum


sol(*map(int, input().split()))
