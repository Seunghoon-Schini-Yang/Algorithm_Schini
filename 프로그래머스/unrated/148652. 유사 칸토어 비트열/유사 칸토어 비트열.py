def solution(n, l, r):
    return count_ones(r) - count_ones(l-1)


def count_ones(x):
    cnt = 0
    mapping = [0, 1, 2, 2, 3]
    ress = []
    thres = 1
    while x:
        x, res = divmod(x, 5)
        ress.append(res)
        thres *= 4
    for i in ress[::-1]:
        thres //= 4
        cnt += thres * mapping[i]
        if i == 2:
            break
    return cnt
