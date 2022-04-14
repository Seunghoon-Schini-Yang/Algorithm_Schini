import sys
input = sys.stdin.readline
import math

def sol(n: int) -> None:
    nums = sorted(map(int, input().split()))
    miny = math.inf
    i = x = 0
    j = y = n-1

    while i<j:
        sum_ij = nums[i]+nums[j]
        if abs(sum_ij) < miny:
            miny = abs(sum_ij)
            x = i; y = j
        if sum_ij > 0:
            j -= 1
        elif sum_ij < 0:
            i += 1
        else:
            break
    print(nums[x],nums[y])


sol(int(input()))
