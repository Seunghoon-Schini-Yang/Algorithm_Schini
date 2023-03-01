def solution(board):
    o = x = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o += 1
            elif board[i][j] == 'X':
                x += 1
    
    if not (o == x or o == x+1):
        return 0

    olink = set(); xlink = set()
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'O':
                olink.add((i, 0)); olink.add((i, 1)); olink.add((i, 2))
            elif board[i][0] == 'X':
                xlink.add((i, 0)); xlink.add((i, 1)); xlink.add((i, 2))
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'O':
                olink.add((0, i)); olink.add((1, i)); olink.add((2, i))
            elif board[0][i] == 'X':
                xlink.add((0, i)); xlink.add((1, i)); xlink.add((2, i))
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            olink.add((0, 0)); olink.add((1, 1)); olink.add((2, 2))
        elif board[0][0] == 'X':
            xlink.add((0, 0)); xlink.add((1, 1)); xlink.add((2, 2))
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            olink.add((0, 2)); olink.add((1, 1)); olink.add((2, 0))
        elif board[0][2] == 'X':
            xlink.add((0, 2)); xlink.add((1, 1)); xlink.add((2, 0))
    
    if (6 <= len(olink) + len(xlink)) or (olink and o == x) or (xlink and x < o):
        return 0
    return 1

