import sys
input = sys.stdin.readline


def testcase() -> str:
    def update_ftree(y: int) -> None:
        while y <= rank:
            ftree[y] += 1
            y += (y & -y)
        return


    def get_ftree(y: int) -> int:
        p_sum = 0
        while y:
            p_sum += ftree[y]
            y ^= (y & -y)
        return p_sum


    answer = 0
    n = int(input())
    xys = [list(map(int, input().split())) for _ in range(n)]
    xys.sort(key=lambda x: x[1])

    # coordinate compression
    temp = xys[0][1]
    xys[0][1] = 1
    rank = 1
    for i in range(1, n):
        if xys[i][1] != temp:
            temp = xys[i][1]
            rank += 1
        xys[i][1] = rank

    # fenwik tree
    ftree = [0] * (rank+1)
    for _, y in sorted(xys, key=lambda x: (-x[0], x[1])):
        answer += get_ftree(y)
        update_ftree(y)

    return str(answer)


if __name__ == '__main__':
    print('\n'.join(testcase() for _ in range(int(input()))))
