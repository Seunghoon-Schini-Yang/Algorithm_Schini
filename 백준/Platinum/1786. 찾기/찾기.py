import sys
input = sys.stdin.readline


def sol(t: str, p: str) -> None:
    p_len = len(p); t_len = len(t)
    if p_len > t_len:
        print(0)
        return
    lps = [0] * p_len
    cnt = 0; idx = list()

    # find LPS in p
    i = 1; j = 0
    while i < p_len:
        if p[i] == p[j]:
            j += 1
            i += 1
        else:
            if not j:
                i += 1
            else:
                lps[i-1] = j
                j = lps[j-1]
    if j > 0:
        lps[i-1] = j

    # find p in t
    i = j = 0
    while i < t_len:
        if p[j] != t[i]:
            if not j:
                i += 1
            else:
                j = lps[j-1]
        else:
            i += 1; j += 1
            if j == p_len:
                cnt += 1
                idx.append(i-p_len+1)
                j = lps[j-1]

    print(len(idx))
    print(' '.join(map(str, idx)))


sol(input().rstrip(), input().rstrip())
