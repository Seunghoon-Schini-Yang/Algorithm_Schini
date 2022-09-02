import sys
input = sys.stdin.readline


def compress(is_y: int) -> int:
    temp = xys[0][is_y]
    xys[0][is_y] = rank = 1
    for i in range(1, N):
        if xys[i][is_y] != temp:
            temp = xys[i][is_y]
            rank += 1
        xys[i][is_y] = rank
    return rank


def query(tree: list, y: int) -> int:
    psum = 0
    while y:
        psum += tree[y]
        y ^= (y & -y)
    return psum


def update(tree: list, y: int, is_add: bool) -> None:
    if not y:
        return
    
    while y <= yrank:
        if is_add:
            tree[y] += 1
        else:
            tree[y] -= 1
        y += (y & -y)
    return


if __name__ == '__main__':
    N = int(input())
    xys = [list(map(int, input().split())) for _ in range(N)]
    rem = pow(10, 9) + 7
    cnt = 0

    # coordinate compression
    xys.sort(key=lambda x: -x[1])
    yrank = compress(1)

    xys.sort(key=lambda x: (x[0], -x[1]))
    compress(0)

    # fenwik tree
    rftree = [0]*(yrank+1)
    for i in range(N):
        update(rftree, xys[i][1], True)

    nxt_xi = 0
    lftree = [0]*(yrank+1)
    for x, y in xys:
        while nxt_xi < N and x+1 >= xys[nxt_xi][0] and (x == xys[nxt_xi][0] or y <= xys[nxt_xi][1]):
            update(rftree, xys[nxt_xi][1], False)
            nxt_xi += 1
        if nxt_xi == N:
            break
        update(lftree, y, True)

        cnt += query(lftree, y-1) * query(rftree, y-1)
        cnt %= rem

    print(cnt)
