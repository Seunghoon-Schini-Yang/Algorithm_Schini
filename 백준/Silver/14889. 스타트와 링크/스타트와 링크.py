import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
weight_l = [list(map(int, input().split())) for _ in range(n)]
weight_d = dict(((i, j), weight_l[i - 1][j - 1] + weight_l[j - 1][i - 1]) for i, j in combinations(range(1, n + 1), 2))

min_i = 10000
synergy_l = [sum(weight_d[tup] for tup in combinations(team, 2)) for team in combinations(range(1, n + 1), n // 2)]

i, j = 0, len(synergy_l) - 1
while i < j:
    min_i = min(min_i, abs(synergy_l[i] - synergy_l[j]))
    i += 1
    j -= 1

print(min_i)