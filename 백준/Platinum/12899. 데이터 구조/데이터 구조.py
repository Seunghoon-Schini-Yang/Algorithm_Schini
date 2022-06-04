# segment tree
import sys
input = sys.stdin.readline
print = sys.stdout.write
N = 2_000_000


def sol(n: int) -> None:
    tree = [0] * (N<<1)

    for _ in range(n):
        t,x = map(int, input().split())
        if t == 1:
            insert(tree, x-1+N)
        else:
            start = N; mid = 3*N>>1; end = N<<1
            while start < mid:
                p_sum = get_sum(tree, start, mid)
                if p_sum < x:
                    x -= p_sum
                    start = mid
                else:
                    end = mid
                mid = (start+end)>>1
            print(f'{start-N+1}\n')
            delete(tree, start)
    return


def insert(tree: list, x: int) -> None:
    while x:
        tree[x] += 1
        x >>= 1
    return


def delete(tree: list, x: int) -> None:
    while x:
        tree[x] -= 1
        x >>= 1
    return


def get_sum(tree: list, start: int, end: int) -> int:
    p_sum = 0
    while start < end:
        if start&1:
            p_sum += tree[start]
            start += 1
        if end&1:
            end ^= 1
            p_sum += tree[end]
        start >>= 1; end >>= 1
    return p_sum


sol(int(input()))
