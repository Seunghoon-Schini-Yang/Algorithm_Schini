# kmp
import sys
input = sys.stdin.readline


def sol(n: int) -> str:
    t = get_diff_arr(input())
    t = t + t[:-1]
    p = get_diff_arr(input())
    lps = failure_fuc(n, p)
    return 'possible' if kmp(n, p, t, lps)  else 'impossible'


def get_diff_arr(angles: str) -> list:
    angles = sorted(map(int, angles.split()))
    # jnooree 님 코드 참고
    return [x-y for x,y in zip(angles[1:] + [angles[0] + 360_000], angles)]


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


def kmp(n: int, p: list, t: list, lps: list) -> bool:
    j = i = 0
    while i < 2*n - 1:
        if p[j] == t[i]:
            j += 1; i += 1
            if j == n:
                return True
        elif not j:
            i += 1
        else:
            j = lps[j-1]

    return False


print(sol(int(input())))
