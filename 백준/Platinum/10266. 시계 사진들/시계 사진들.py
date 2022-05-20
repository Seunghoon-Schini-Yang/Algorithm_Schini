# kmp
import sys
input = sys.stdin.readline


def get_diff_arr(n: int, angles: str) -> list:
    angles = sorted(map(int, angles.split()))
    # diff = [angles[i]-angles[i-1] for i in range(1, n)]
    diff = [0] * n
    for i in range(n-1):
        diff[i] = angles[i+1] - angles[i]
    diff[-1] = angles[0] + 360_000 - angles[-1]
    return diff


def failure_fuc(n: int, p: list) -> list:
    lps = [0] * n
    j = 0; i = 1

    while i < n:
        if p[j] == p[i]:
            j += 1; i += 1
        elif not j:
            i += 1
        else:
            lps[i-1] = j
            j = lps[j-1]
    if j > 0:
        lps[i-1] = j
    
    return lps


def kmp(n: int, p: list, t: list, lps: list) -> str:
    j = i = 0
    while i < 2*n - 1:
        if p[j] == t[i]:
            j += 1; i += 1
            if j == n:
                return 'possible'
        elif not j:
            i += 1
        else:
            j = lps[j-1]

    return 'impossible'


def sol(n: int) -> str:
    t = get_diff_arr(n, input())
    t = t + t[:-1]
    p = get_diff_arr(n, input())
    lps = failure_fuc(n, p)
    return kmp(n, p, t, lps)


print(sol(int(input())))
