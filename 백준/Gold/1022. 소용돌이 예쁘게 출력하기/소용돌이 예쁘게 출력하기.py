import sys
input = sys.stdin.readline


def _calc(r, c):
    is_r = True if abs(c) <= abs(r) else False
    maxy = max(abs(r), abs(c))
    edge = ((maxy<<1)+1)**2
    if is_r:
        if r > 0:
            return edge - (maxy-c)
        return edge - (maxy<<2) - (maxy+c)
    else:
        if c > 0:
            return edge - 3*(maxy<<1) - (maxy+r)
        return edge - (maxy<<1) - (maxy-r)


class Swirl():
    def __init__(self, r1, c1, r2, c2):
        values = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
        for i, r in enumerate(range(r1, r2+1)):
            for j, c in enumerate(range(c1, c2+1)):
                values[i][j] = _calc(r, c)
        maxy = max(max(row) for row in values)
        maxy_len = len(str(maxy))
        self.values = '\n'.join(' '.join(map(lambda x: str(x).rjust(maxy_len, ' '), row)) for row in values)


if __name__ == '__main__':
    board = Swirl(*map(int, input().split()))
    print(board.values)
