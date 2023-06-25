def solution(rows, columns, queries):
    def rotate(x1, y1, x2, y2):
        x1 -= 1; y1 -= 1; x2 -=1; y2 -= 1
        miny = tmp = board[x1][y1]
        for r in range(x1, x2):
            board[r][y1] = board[r+1][y1]
            miny = min(miny, board[r][y1])
        for c in range(y1, y2):
            board[x2][c] = board[x2][c+1]
            miny = min(miny, board[x2][c])
        for r in range(x2, x1, -1):
            board[r][y2] = board[r-1][y2]
            miny = min(miny, board[r][y2])
        for c in range(y2, y1, -1):
            board[x1][c] = board[x1][c-1]
            miny = min(miny, board[x1][c])
        board[x1][y1+1] = tmp
        return miny
    
    
    maxy = rows * columns
    board = [[r+c for c in range(columns)] for r in range(1, maxy, columns)]
    return [rotate(*q) for q in queries]