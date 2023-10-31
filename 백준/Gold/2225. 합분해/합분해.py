from math import comb

n, k = map(int, input().split())
print(comb(n+k-1, n) % int(1e9))