def solution(board):
    N, M = len(board), len(board[0])
    for r in range(1, N):
        for c in range(M):
            if not board[r][c]:
                continue
            board[r][c] = board[r-1][c] + 1
    
    answer = 0
    for row in board:
        row.append(0)
        stack = []
        for h in row:
            acc = 0
            while stack and h < stack[-1][0]:
                ch, cnt = stack.pop()
                if ch <= answer:
                    stack = []
                    break
                acc += cnt
                if ch <= acc:
                    answer = ch
                    stack = []
                    break
            acc += 1
            if h <= answer:
                stack = []
            elif stack and stack[-1][0] == h:
                stack[-1][1] += acc
            else:
                stack.append([h, acc])

    return answer ** 2
