import sys
input = sys.stdin.readline


class Chess():
    def __init__(self, N):
        self.board = [list(map(lambda x: int(x)^1, input().split())) for _ in range(N)]
        self.N, self.n = N, N**2
        self.even = []
        self.odd = []
        for i in range(self.n):
            r, c = divmod(i, self.N)
            if (r+c)&1:
                self.odd.append((r, c))
            else:
                self.even.append((r, c))
        
        ans = 0
        self.maxy = self.cur = 0
        self._callback(self.odd)()
        ans += self.maxy
        self.maxy = self.cur = 0
        self._callback(self.even)()
        ans += self.maxy
        self.maxy = ans


    def _callback(self, arr):
        def _backtrack(start_idx=0):
            for i in range(start_idx, len(arr)):
                r, c = arr[i]
                if self.board[r][c]:
                    continue

                self.cur += 1
                self.maxy = max(self.maxy, self.cur)

                locs = self._get_avail_locs(r, c)
                _backtrack(i+1)

                self.cur -= 1
                for rr, cc in locs:
                    self.board[rr][cc] = 0
        return _backtrack
    

    def _get_avail_locs(self, r, c):
        locs = []
        rr, cc = r, c
        while 0 < cc and rr < self.N-1:
            cc -= 1
            rr += 1
            if not self.board[rr][cc]:
                locs.append((rr, cc))
                self.board[rr][cc] = 1
        rr, cc = r, c
        while cc < self.N-1 and rr < self.N-1:
            cc += 1
            rr += 1
            if not self.board[rr][cc]:
                locs.append((rr, cc))
                self.board[rr][cc] = 1
        return locs


if __name__ == '__main__':
    bishops = Chess(int(input()))
    print(bishops.maxy)
