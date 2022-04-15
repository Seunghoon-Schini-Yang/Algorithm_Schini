import sys
input = sys.stdin.readline
from itertools import product
from bisect import bisect_right

def sol(n: int, c: int) -> int:
    nums = map(int, input().split())
    fst_h = list(next(nums) for _ in range(n>>1))
    snd_h = list(next(nums) for _ in range(n-(n>>1)))

    fst_sub_sum = [sum(fst_h[i] if comb[i] else 0 for i in range(n>>1)) for comb in product(*((0,1) for _ in range(n>>1)))]
    snd_sub_sum = [sum(snd_h[i] if comb[i] else 0 for i in range(n-(n>>1))) for comb in product(*((0,1) for _ in range(n-(n>>1))))]

    fst_sub_sum.sort()

    return sum(bisect_right(fst_sub_sum, c-v) for v in snd_sub_sum)


print(sol(*map(int, input().split())))
