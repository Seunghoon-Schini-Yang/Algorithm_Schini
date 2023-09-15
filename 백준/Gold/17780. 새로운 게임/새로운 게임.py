import sys
input = sys.stdin.readline


class Chess():
    def __init__(self, N, K):
        board = [list(map(int, input().split())) for _ in range(N)]
        p_board = [[[] for _ in range(N)] for _ in range(N)]
        p_info = [(0, 0, 0, 0) for _ in range(K)]
        for i in range(K):
            r, c, d = map(lambda x: int(x)-1, input().split())
            p_board[r][c].append(i)
            p_info[i] = [r, c, d, 0]
        
        game_clear = False
        dr, dc = (0, 0, -1, 1), (1, -1, 0, 0)
        turn = 1
        while turn <= 1000:
            for i in range(K):
                if p_info[i][3]:
                    continue
                r, c, d, _ = p_info[i]
                rr, cc = r+dr[d], c+dc[d]
                if rr < 0 or N <= rr or cc < 0 or N <= cc or board[rr][cc] == 2:
                    d += -1 if d&1 else 1
                    p_info[i][2] = d
                    rr, cc = r+dr[d], c+dc[d]

                if rr < 0 or N <= rr or cc < 0 or N <= cc or board[rr][cc] == 2:
                    continue
                if board[rr][cc] == 1:
                    p_board[r][c] = p_board[r][c][::-1]
                idx = len(p_board[rr][cc])
                p_board[rr][cc].extend(p_board[r][c])
                if 4 <= len(p_board[rr][cc]):
                    game_clear = True
                    break
                for i, piece in enumerate(p_board[r][c], start=idx):
                    p_info[piece][0], p_info[piece][1], p_info[piece][3] = rr, cc, i
                p_board[r][c] = []
            
            if game_clear:
                break
            turn += 1

        self.turn = turn if turn <= 1000 else -1



if __name__ == '__main__':
    game = Chess(*map(int, input().split()))
    print(game.turn)
