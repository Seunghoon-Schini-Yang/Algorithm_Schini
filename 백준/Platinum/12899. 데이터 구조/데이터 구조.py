import sys
input = sys.stdin.readline
print = sys.stdout.write


def add_tree(x: int) -> None:
    while x:
        seg_tree[x] += 1
        x >>= 1


def del_tree(x: int) -> int:
    i = 1
    seg_tree[i] -= 1
    while (i<<1) < N:
        if seg_tree[i<<1] < x:
            x -= seg_tree[i<<1]
            i = (i<<1)^1
        else:
            i <<= 1
        seg_tree[i] -= 1
    return i-A


if __name__ == '__main__':
    N = pow(2,22); A = (N>>1)-1
    seg_tree = [0]*N
    for _ in range(int(input())):
        T,X = map(int, input().split())
        if T == 1:
            add_tree(X+A)
        else:
            print(f'{del_tree(X)}\n')
