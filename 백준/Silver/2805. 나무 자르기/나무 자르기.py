import sys
input = sys.stdin.readline
from collections import Counter

def solution(n: int, m: int) -> int:
    trees = [*map(int, input().split())]
    counter = Counter(trees)
    trees = sorted(set(trees), reverse=True)
    trees.append(0)
    res = trees[0]
    width = 0

    for i in range(len(trees) - 1):
        width += counter[trees[i]]
        if (gap := trees[i] - trees[i + 1]) * width >= m:
            res -= m // width + (m % width != 0)
            break
        else:
            m -= gap * width
            res -= gap
    
    return res


print(solution(*map(int, input().split())))
