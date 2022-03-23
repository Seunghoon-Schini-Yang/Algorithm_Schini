import sys
input = sys.stdin.readline

def solution(n: int, m: int) -> int:
    trees = [*map(int, input().split())]
    bottom, top = 0, max(trees)
    while bottom <= top:
        mid = (bottom + top) // 2
        cut_off = sum(tree - mid if tree > mid else 0 for tree in trees)
        if cut_off > m:
            bottom = mid + 1
        elif cut_off < m:
            top = mid - 1
        else:
            return mid
    return top


print(solution(*map(int, input().split())))
