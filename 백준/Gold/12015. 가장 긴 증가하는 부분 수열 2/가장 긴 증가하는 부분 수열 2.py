import sys
input = sys.stdin.readline
from bisect import bisect_left

def solution() -> int:
    seq = map(int, input().split())
    inc = [next(seq)]
    for x in seq:
        if x > inc[-1]:
            inc.append(x)
        else:
            inc[bisect_left(inc, x)] = x

    return len(inc)


input()
print(solution())
