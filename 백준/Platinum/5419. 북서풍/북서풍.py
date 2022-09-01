import sys
input = sys.stdin.readline


def testcase() -> int:
    def update_segtree(idx: int) -> None:
        while idx:
            segtree[idx] += 1
            idx >>= 1
        return


    def get_segtree(e: int) -> int:
        p_sum = 0
        s = tree_len
        while s < e:
            if s & 1:
                p_sum += segtree[s]
                s += 1
            s >>= 1
            if e & 1:
                e ^= 1
                p_sum += segtree[e]
            e >>= 1
        return p_sum


    answer = 0
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    xys.sort(key=lambda x: x[1])

    # coordinate compression
    temp = xys[0][1]
    rank = xys[0][1] = 0
    for i in range(1, n):
        if xys[i][1] != temp:
            temp = xys[i][1]
            rank += 1
        xys[i][1] = rank

    # segment tree
    tree_len = rank+1
    segtree = [0] * (tree_len*2)
    for _, y in sorted(xys, key=lambda x: (-x[0], x[1])):
        answer += get_segtree(y+tree_len+1)
        update_segtree(y+tree_len)

    return str(answer)


if __name__ == '__main__':
    print('\n'.join(testcase() for _ in range(int(input()))))
