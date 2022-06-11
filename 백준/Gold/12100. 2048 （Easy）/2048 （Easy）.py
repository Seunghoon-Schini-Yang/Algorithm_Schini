import sys
input = sys.stdin.readline
from copy import deepcopy


def sol(n: int) -> int:
    def dfs(board: list, cnt: int) -> int:
        if cnt == 5:
            return max(map(max, board))

        return max(dfs(shift(deepcopy(board), i, j), cnt+1) for i in range(2) for j in range(2))


    def shift(board: list, dir: int, sign: int) -> list:
        if dir:
            for row in range(n):
                pointer = pointers[sign]
                for col in range(start[sign], end[sign], diff[sign]):
                    if board[row][col]:
                        if board[row][col] == board[row][pointer]:
                            board[row][pointer] <<= 1
                            board[row][col] = 0
                            pointer += diff[sign]
                        elif not board[row][pointer]:
                            board[row][pointer] = board[row][col]
                            board[row][col] = 0
                        else:
                            pointer += diff[sign]
                            tmp = board[row][col]
                            board[row][col] = 0
                            board[row][pointer] = tmp
        else:
            for col in range(n):
                pointer = pointers[sign]
                for row in range(start[sign], end[sign], diff[sign]):
                    if board[row][col]:
                        if board[row][col] == board[pointer][col]:
                            board[pointer][col] <<= 1
                            board[row][col] = 0
                            pointer += diff[sign]
                        elif not board[pointer][col]:
                            board[pointer][col] = board[row][col]
                            board[row][col] = 0
                        else:
                            pointer += diff[sign]
                            tmp = board[row][col]
                            board[row][col] = 0
                            board[pointer][col] = tmp
        return board


    # left-right, up-down
    start = [1, n-2]
    end = [n, -1]
    diff = [1, -1]
    pointers = [0, n-1]

    board = [list(map(int, input().split())) for _ in range(n)]
    return dfs(board, 0)


print(sol(int(input())))
