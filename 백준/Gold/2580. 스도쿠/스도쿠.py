class Sudoku():
    def __init__(self):
        self.board = [list(map(int, input().split())) for _ in range(9)]
        self.init_memo()
        self.backtrack(0)
        
        
    def init_memo(self):
        board = self.board
        rmemo = [[False]*10 for _ in range(9)]
        cmemo = [[False]*10 for _ in range(9)]
        bmemo = [[False]*10 for _ in range(9)]
        es = []
        for r in range(9):
            for c in range(9):
                cur = board[r][c]
                if cur:
                    rmemo[r][cur] = True
                    cmemo[c][cur] = True
                    bmemo[(r//3)*3 + (c//3)][cur] = True
                else:
                    es.append((r, c))
        self.rmemo, self.cmemo, self.bmemo = rmemo, cmemo, bmemo
        self.es, self.esl = es, len(es)

    
    def backtrack(self, i):
        if i == self.esl:
            return True
        r, c = self.es[i]
        for x in range(1, 10):
            if not self.rmemo[r][x] and not self.cmemo[c][x] and not self.bmemo[(r//3)*3 + (c//3)][x]:
                self.board[r][c] = x
                self.rmemo[r][x] = self.cmemo[c][x] = self.bmemo[(r//3)*3 + (c//3)][x] = True
                if self.backtrack(i+1):
                    return True
                self.rmemo[r][x] = self.cmemo[c][x] = self.bmemo[(r//3)*3 + (c//3)][x] = False
                self.board[r][c] = 0
                

if __name__ == '__main__':
    sudoku = Sudoku()
    print('\n'.join(' '.join(map(str, row)) for row in sudoku.board))
