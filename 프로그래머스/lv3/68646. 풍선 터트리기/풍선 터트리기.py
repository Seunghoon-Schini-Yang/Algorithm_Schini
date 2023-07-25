def solution(a):
    n = len(a)
    if n <= 2:
        return n
    lmin = a[:]
    rmin = a[:]
    for i in range(1, n):
        if lmin[i-1] < lmin[i]:
            lmin[i] = lmin[i-1]
        if rmin[~(i-1)] < rmin[~i]:
            rmin[~i] = rmin[~(i-1)]     
    return sum(0 if a[i] > rmin[i+1] and a[i] > lmin[i-1] else 1 for i in range(1, n-1)) + 2
