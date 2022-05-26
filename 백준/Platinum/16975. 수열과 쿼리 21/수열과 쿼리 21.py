# segment tree (list)
# 이 문제에선 update와 select의 기능이 서로 반대
import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int) -> None:
    tree = [0] * (2*n)
    tree[n:] = list(map(int, input().split()))

    for _ in range(int(input())):
        a, *x = map(int, input().split())
        if a == 1:
            query_update(n, tree, *x)
        else:
            print(f'{query_select(tree, n+x[0]-1)}\n')
    return


def query_update(n: int, tree: list, i: int, j: int, k: int) -> None:
    i += n-1; j += n
    while i < j:
        if i&1:
            tree[i] += k
            i += 1
        if j&1:
            j -= 1
            tree[j] += k
        i >>= 1; j >>= 1
    return


def query_select(tree: list, x: int) -> int:
    val = 0
    while x:
        val += tree[x]
        x >>= 1
    return val


sol(int(input()))
