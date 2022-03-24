import sys
input = sys.stdin.readline


def solution(n: int) -> int:
    seq = map(int, input().split())
    inc, inc_last_idx = [next(seq)], 0
    for _ in range(n-1):
        x = next(seq)
        if x > inc[-1]:
            inc.append(x)
            inc_last_idx += 1
        else:
            lo, hi = 0, inc_last_idx
            while lo <= hi:
                mid = (lo + hi)//2
                if x > inc[mid]:
                    lo = mid+1
                else:
                    hi = mid-1
            inc[lo] = x

    return inc_last_idx + 1


print(solution(int(input())))
