def solution(seq, k):
    if seq[0] == k:
        return [0, 0]
    n = l = s = e = len(seq)
    i, j = 0, 1
    acc = seq[0]
    while i < j and j < n:
        if acc == k:
            if j-1-i < l:
                s, e = i, j-1
                l = e-s
            acc += seq[j]
            j += 1
            i += 2
            if j < i:
                return [s, e]
            acc -= seq[i-1] + seq[i-2]
        elif acc < k:
            acc += seq[j]
            j += 1
        else:
            acc -= seq[i]
            i += 1
    while i < j and k <= acc:
        if acc == k:
            if j-1-i < l:
                s, e = i, j-1
            return [s, e]
        acc -= seq[i]
        i += 1
    return [s, e]