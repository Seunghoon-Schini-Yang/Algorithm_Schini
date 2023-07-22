import sys
input = sys.stdin.readline
from copy import deepcopy


class Office():
    def __init__(self, N, M):
        self.blind = 64
        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        board = [list(map(int, input().split())) for _ in range(N)]
        self.cctvs = []
        for r in range(N):
            for c in range(M):
                if board[r][c] == 0 or board[r][c] == 6 or board[r][c] == 7:
                    continue
                if board[r][c] == 5:
                    for i in range(4):
                        cr, cc = r, c
                        while 0 <= cr+dr[i] < N and 0 <= cc+dc[i] < M:
                            cr += dr[i]; cc += dc[i]
                            if board[cr][cc] == 6:
                                break
                            if board[cr][cc] == 0:
                                board[cr][cc] = 7
                    continue
                self.cctvs.append((r, c))
        self.cctvs_len = len(self.cctvs)
        self.N, self.M = N, M
        self.dr, self.dc = dr, dc
        self.deploy(board, 0)
    
    
    def deploy(self, board, depth):
        if depth == self.cctvs_len:
            self.blind =\
            min(self.blind, sum(board[r][c] == 0 for c in range(self.M) for r in range(self.N)))
            return
        
        r, c = self.cctvs[depth]
        _type = board[r][c]
        if _type == 1:
            seqs = [[0], [1], [2], [3]]
        elif _type == 2:
            seqs = [[0, 1], [2, 3]]
        elif _type == 3:
            seqs = [[0, 2], [0, 3], [1, 2], [1, 3]]
        else:
            seqs = [[0, 1, 2], [0, 1, 3], [0, 2, 3], [1, 2, 3]]
        for seq in seqs:
            nboard = deepcopy(board)
            for i in seq:
                cr, cc = r, c
                while 0 <= cr+self.dr[i] < self.N and 0 <= cc+self.dc[i] < self.M:
                    cr += self.dr[i]; cc += self.dc[i]
                    if nboard[cr][cc] == 6:
                        break
                    if nboard[cr][cc] == 0:
                        nboard[cr][cc] = 7
            self.deploy(nboard, depth+1)


if __name__ == '__main__':
    office = Office(*map(int, input().split()))
    print(office.blind)
