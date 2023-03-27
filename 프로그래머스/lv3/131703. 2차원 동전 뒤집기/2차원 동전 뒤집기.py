def solution(beginning, target):
    nr, nc = len(target), len(target[0])

    to_ones = [[b == t for b, t in zip(beg, tar)] for beg, tar in zip(beginning, target)]
    mcnt = 20
    if to_ones[0][0]:
        mcnt = 2
        for r in range(1, nr):
            to_ones[r][0] ^= 1
        for c in range(1, nc):
            to_ones[0][c] ^= 1
        for r in range(1, nr):
            if to_ones[r][0]:
                continue
            mcnt += 1
            for c in range(nc):
                to_ones[r][c] ^= 1
        for c in range(1, nc):
            if to_ones[0][c]:
                continue
            mcnt += 1
            for r in range(nr):
                to_ones[r][c] ^= 1
    
    to_ones = [[b == t for b, t in zip(beg, tar)] for beg, tar in zip(beginning, target)]
    rcnt = 0
    for c in range(nc):
        if to_ones[0][c]:
            continue
        rcnt += 1
        for r in range(nr):
            to_ones[r][c] ^= 1
    for r in range(1, nr):
        if to_ones[r][0]:
            continue
        rcnt += 1
        for c in range(nc):
            to_ones[r][c] ^= 1

    to_ones = [[b == t for b, t in zip(beg, tar)] for beg, tar in zip(beginning, target)]
    ccnt = 0
    for r in range(nr):
        if to_ones[r][0]:
            continue
        ccnt += 1
        for c in range(nc):
            to_ones[r][c] ^= 1
    for c in range(1, nc):
        if to_ones[0][c]:
            continue
        ccnt += 1
        for r in range(nr):
            to_ones[r][c] ^= 1

    for r in range(1, nr):
        for c in range(1, nc):
            if not to_ones[r][c]:
                return -1

    return min(rcnt, ccnt, mcnt)
