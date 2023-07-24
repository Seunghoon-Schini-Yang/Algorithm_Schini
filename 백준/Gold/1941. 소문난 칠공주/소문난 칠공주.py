import sys
input = sys.stdin.readline
from itertools import combinations


def _adjs(r, c):
    if 0 < r:  yield r-1, c
    if 0 < c:  yield r, c-1
    if r < 4:  yield r+1, c
    if c < 4:  yield r, c+1


def _is_connected(coords):
    rest = set(coords[1:])
    stack = [coords[0]]
    while stack:
        for r, c in _adjs(*stack.pop()):
            if (r, c) in rest:
                stack.append((r, c))
                rest.remove((r, c))
    return False if rest else True


class Election():
    def __init__(self):
        district = [input().rstrip() for _ in range(5)]
        cnt = 0
        for seq in combinations(((r, c) for c in range(5) for r in range(5)), 7):
            if sum(1 if district[r][c] == 'S' else 0 for r, c in seq) < 4:
                continue
            if _is_connected(seq):
                cnt += 1
        self.answer = cnt


if __name__ == '__main__':
    elec = Election()
    print(elec.answer)
