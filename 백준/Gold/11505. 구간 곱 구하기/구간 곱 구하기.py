# segment tree (list)
# 구간 합 구하기 : wlsxkr77 님 코드 참고
import sys
input = sys.stdin.readline
print = sys.stdout.write
rem = 1_000_000_007


def sol(n: int, m: int, k: int) -> None:
    tree = [0] * (2*n)
    tree[n:] = [int(input()) for _ in range(n)]
    for i in range(n-1, 0, -1):
        tree[i] = tree[i<<1]%rem * tree[i<<1|1]%rem

    for _ in range(m+k):
        a,b,c = map(int, input().split())
        if a&1:
            update_tree(tree, n+b-1, c)
        else:
            print(f'{partial_prod(tree, n+b-1, n+c)}\n')
    return


def update_tree(tree: list, idx: int, val: int) -> None:
    tree[idx] = val
    idx >>= 1
    while idx:
        tree[idx] = tree[idx<<1]%rem * tree[idx<<1|1]%rem
        idx >>= 1
    return


def partial_prod(tree: list, s: int, e: int) -> int:
    p_prod = 1
    while s < e:
        if s&1:
            p_prod *= tree[s]
            s += 1
        if e&1:
            e ^= 1
            p_prod *= tree[e]
        s >>= 1; e >>= 1
    return p_prod % rem


sol(*map(int, input().split()))
