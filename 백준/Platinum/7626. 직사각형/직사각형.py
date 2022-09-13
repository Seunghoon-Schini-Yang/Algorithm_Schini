import sys
input = sys.stdin.readline


def line_update(start: int, end: int, is_start: bool) -> None:
    def sum_update(idx: int, val: int) -> None:
        linetree[idx][1] += 1
        if linetree[idx][1] == 1:
            linetree[idx][0] += val
            idx >>= 1
            while idx and not linetree[idx][1]:
                linetree[idx][0] += val
                idx >>= 1
        return


    def sum_minus_update(idx: int) -> None:
        linetree[idx][1] -= 1
        if not linetree[idx][1]:
            deduct = linetree[idx][0]
            if (idx<<1) < 2*y_odr:
                deduct -= linetree[idx<<1][0] + linetree[(idx<<1)^1][0]
            while idx and not linetree[idx][1]:
                linetree[idx][0] -= deduct
                idx >>= 1
        return
    

    while start < end:
        if start&1:
            if is_start:
                sum_update(start, sumtree[start] - linetree[start][0])
            else:
                sum_minus_update(start)
            start += 1
        start >>= 1

        if end&1:
            end -= 1
            if is_start:
                sum_update(end, sumtree[end] - linetree[end][0])
            else:
                sum_minus_update(end)
        end >>= 1

    return


if __name__ == '__main__':
    N = int(input())
    xxyys = [list(map(int, input().split())) for _ in range(N)]

    # compress coordinate
    ys = list()
    for i in range(N):
        ys.append((xxyys[i][2], i, 2)); ys.append((xxyys[i][3], i, 3))

    ys.sort(key=lambda y: y[0])
    tmp = ys[0][0]
    y_odr = xxyys[ys[0][1]][2] = 0
    y_real = [tmp]

    for y, i, loc in ys[1:]:
        if y != tmp:
            tmp = y
            y_real.append(tmp)
            y_odr += 1
        xxyys[i][loc] = y_odr

    # break start-end line
    xs = [0] * (2*N)
    for i in range(N):
        xs[2*i] = (xxyys[i][0], True, xxyys[i][2], xxyys[i][3])
        xs[2*i+1] = (xxyys[i][1], False, xxyys[i][2], xxyys[i][3])
    xs.sort(key=lambda x: x[0])

    # segment tree
    linetree = [[0, 0] for _ in range(2*y_odr)]
    sumtree = [0] * (2*y_odr)
    sumtree[y_odr:] = [y_real[i+1] - y_real[i] for i in range(y_odr)]
    for i in range(y_odr-1, 0, -1):
        sumtree[i] = sumtree[i<<1] + sumtree[(i<<1)^1]

    # get area
    area = 0
    tmp = xs[0][0]
    for x, is_start, y1, y2 in xs:
        if x != tmp:
            area += (x-tmp) * linetree[1][0]
            tmp = x
        line_update(y1+y_odr, y2+y_odr, is_start)

    print(area)
