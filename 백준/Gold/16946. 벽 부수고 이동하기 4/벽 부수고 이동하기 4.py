import sys
input = sys.stdin.readline
from copy import deepcopy


class Maapp():
    def __init__(self, N, M):
        self.board = [list(map(int, input().rstrip())) for _ in range(N)]
        self.answer = deepcopy(self.board)
        group_count = [0, 0]
        self.N, self.M = N, M
        n_grp = 2
        for r in range(N):
            for c in range(M):
                if self.board[r][c]:
                    continue
                group_count.append(self._crash(n_grp, r, c))
                n_grp += 1
        for r in range(N):
            for c in range(M):
                if not self.answer[r][c]:
                    continue
                n_grp = {self.board[rr][cc] for rr, cc in self._adjs(r, c)}
                self.answer[r][c] = (sum(group_count[grp] for grp in n_grp) + 1) % 10

    
    def _crash(self, grp, r, c):
        cnt = 1
        self.board[r][c] = grp
        stack = [(r, c)]
        while stack:
            r, c = stack.pop()
            for rr, cc in self._adjs(r, c):
                if self.board[rr][cc]:
                    continue
                self.board[rr][cc] = grp
                cnt += 1
                stack.append((rr, cc))
        return cnt


    def _adjs(self, r, c):
        if r > 0:  yield r-1, c
        if c > 0:  yield r, c-1
        if r < self.N-1:  yield r+1, c
        if c < self.M-1:  yield r, c+1


if __name__ == '__main__':
    _map = Maapp(*map(int, input().split()))
    print('\n'.join(''.join(map(str, row)) for row in _map.answer))
