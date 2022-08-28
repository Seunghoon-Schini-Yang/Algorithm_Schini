import sys
input = sys.stdin.readline


if __name__ == '__main__':
    N, dist = map(int, input().split())

    rev_psngr = list()
    for _ in range(N):
        sp, ep = map(int, input().split())
        if sp <= ep:
            continue
        rev_psngr.append((ep, sp))
    rev_psngr.sort()

    if rev_psngr:
        s, e = rev_psngr[0]

        for cs, ce in rev_psngr[1:]:
            if e <= cs:
                dist += 2 * (e - s)
                s, e = cs, ce
            elif e < ce:
                e = ce
        dist += 2 * (e - s)

    print(dist)
