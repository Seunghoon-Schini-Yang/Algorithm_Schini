import sys
input = sys.stdin.readline
import math

def sol(n: int, s: int) -> int:
    nums = list(map(int, input().split()))
    i = j = sum_ij = 0
    min_len = math.inf
    
    while j <= n:
        if min_len == 1:
            return 1
            
        if sum_ij < s:
            if j == n:
                break
            sum_ij += nums[j]
            j += 1
        else:
            if j-i < min_len:
                min_len = j-i
            sum_ij -= nums[i]
            i += 1
    
    return 0 if math.isinf(min_len) else min_len


print(sol(*map(int, input().split())))
