import sys
input = sys.stdin.readline
from itertools import permutations


class Parenthesis():
    def __init__(self, N):
        eq = input().rstrip()
        if N == 1:
            self.maxy = int(eq)
        else:
            self.symbols = eq[1::2]
            self.values = list(map(int, eq[::2]))
            N >>= 1
            self.n = N+1
            self.maxy = max(self._get_value(seq) for seq in permutations(range(N), N))


    def _get_value(self, seq):
        depth = [-1] * self.n
        cur = self.values[:]

        def _calc(x, y, sym):
            if sym == '*':
                return x * y
            if sym == '-':
                return x - y
            return x + y
        
        def _find(x):
            if depth[x] < 0:
                return x
            depth[x] = _find(depth[x])
            return depth[x]
        
        def _union(x, y):
            x, y = _find(x), _find(y)
            val = _calc(cur[x], cur[y], self.symbols[i])
            if depth[x] < depth[y]:
                depth[y] = x
                cur[x] = val
            else:
                if depth[x] == depth[y]:
                    depth[y] -= 1
                depth[x] = y
                cur[y] = val
            return val

        for i in seq:
            val = _union(i, i+1)
        return val


if __name__ == '__main__':
    equation = Parenthesis(int(input()))
    print(equation.maxy)
