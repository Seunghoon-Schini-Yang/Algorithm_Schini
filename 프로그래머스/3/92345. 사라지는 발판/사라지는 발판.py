def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    def adjs(r, c):
        if r > 0:  yield r-1, c
        if c > 0:  yield r, c-1
        if r < n-1:  yield r+1, c
        if c < m-1:  yield r, c+1

    def recur(board, aloc, bloc, turn):
        loc = bloc if turn else aloc
        if not board[loc[0]][loc[1]]:
            return 0, 0, turn^1
        
        cur_mov = cur_other = 0
        step = False
        cur_winner = turn^1

        board[loc[0]][loc[1]] = 0
        for r, c in adjs(*loc):
            if not board[r][c]:
                continue
            step = True
            amov, bmov, winner = recur(
                board,
                aloc if turn else [r, c],
                [r, c] if turn else bloc,
                turn^1
            )
            mov, other = (bmov, amov) if turn else (amov, bmov)

            if cur_winner ^ turn:
                if cur_winner ^ winner:
                    cur_mov, cur_other, cur_winner = mov, other, turn
                    continue
                cur_mov, cur_other = (mov, other) if mov >= cur_mov else (cur_mov, cur_other)
            else:
                if cur_winner ^ winner:
                    continue
                cur_mov, cur_other = (mov, other) if mov < cur_mov else (cur_mov, cur_other)
        
        board[loc[0]][loc[1]] = 1
        if not step:
            return cur_mov, cur_other, cur_winner
        return (cur_other, cur_mov+1, cur_winner) if turn else (cur_mov+1, cur_other, cur_winner)
    
    a, b, _ = recur(board, aloc, bloc, 0)
    return a+b
