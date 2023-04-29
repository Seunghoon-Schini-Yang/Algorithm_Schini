from itertools import product
from copy import deepcopy
import sys


def solution(clockHands):
    def rotate(r, c, dgr):
        
        return
    
    
    answer = sys.maxsize
    n = len(clockHands)
    dr, dc = [1, 0, -1, 0, 0], [0, 1, 0, -1, 0]
    for case in product(range(4), repeat=n):
        cur = 0
        board = deepcopy(clockHands)
        for c in range(n):
            if not case[c]:
                continue
            cur += case[c]
            for rr, cc in zip(dr, dc):
                if 0 <= rr < n and 0 <= c+cc < n:
                    board[rr][c+cc] = (board[rr][c+cc] + case[c]) % 4
        for r in range(1, n):
            for c in range(n):
                dgr = (4-board[r-1][c]) % 4
                if not dgr:
                    continue
                cur += dgr
                for rr, cc in zip(dr, dc):
                    if 0 <= r+rr < n and 0 <= c+cc < n:
                        board[r+rr][c+cc] = (board[r+rr][c+cc] + dgr) % 4
        if any(board[-1]):
            continue
        answer = min(cur, answer)

    return answer