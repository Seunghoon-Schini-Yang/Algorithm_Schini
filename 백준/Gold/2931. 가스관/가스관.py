import sys
input = sys.stdin.readline


class Pipe():
    def __init__(self, R, C):
        self.R, self.C = R, C
        dd = [[-1, 0, 1, 0], [0, 1, 0, -1]]
        mapping = {0: 2, 1: 3, 2: 0, 3: 1}
        r, c = self._init_board()
        for i in range(4):
            if 0 <= r+dd[0][i] < self.R and 0 <= c+dd[1][i] < self.C:
                if self.board[r+dd[0][i]][c+dd[1][i]] not in ('.', 'Z'):
                    r, c, inway = r+dd[0][i], c+dd[1][i], mapping[i]
                    break
        while self.board[r][c] != '.':
            inway = self._get_next_inway(inway, r, c)
            r, c = r+dd[0][mapping[inway]], c+dd[1][mapping[inway]]
        
        links = []
        poss = [
            ("|", "+", "1", "4"), ("-", "+", "3", "4"), ("|", "+", "2", "3"), ("-", "+", "1", "2")
        ]
        for i in range(4):
            if 0 <= r+dd[0][i] < self.R and 0 <= c+dd[1][i] < self.C:
                if self.board[r+dd[0][i]][c+dd[1][i]] in poss[i]:
                    links.append(i)
        if len(links) == 4:
            shape = "+"
        else:
            if links == [0, 1]:
                shape = "2"
            elif links == [0, 2]:
                shape = "|"
            elif links == [0, 3]:
                shape = "3"
            elif links == [1, 2]:
                shape = "1"
            elif links == [1, 3]:
                shape = "-"
            elif links == [2, 3]:
                shape = "4"
        self.hacked = (r+1, c+1, shape)


    def _init_board(self):
        self.board = [input().rstrip() for _ in range(self.R)]
        for r in range(self.R):
            for c in range(self.C):
                if self.board[r][c] == 'M':
                    return (r, c)

    
    def _get_next_inway(self, inway, r, c):
        if self.board[r][c] == '|':
            return 2 if inway == 2 else 0
        if self.board[r][c] == '-':
            return 3 if inway == 3 else 1
        if self.board[r][c] == '+':
            return inway
        if self.board[r][c] == '1':
            return 3 if inway == 2 else 0
        if self.board[r][c] == '2':
            return 3 if inway == 0 else 2
        if self.board[r][c] == '3':
            return 1 if inway == 0 else 2
        if self.board[r][c] == '4':
            return 1 if inway == 2 else 0


if __name__ == '__main__':
    pipes = Pipe(*map(int, input().split()))
    print(*pipes.hacked)
