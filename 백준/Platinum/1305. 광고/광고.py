# kmp
import sys
input = sys.stdin.readline


def sol(n: int) -> int:
    s = input().rstrip()
    lps = [0] * n

    j = 0; i = 1
    while i < n:
        if s[j] == s[i]:
            j += 1; i += 1
        else:
            if not j:
                i += 1
            else:
                lps[i-1] = j
                j = lps[j-1]
    return n-j


print(sol(int(input())))
