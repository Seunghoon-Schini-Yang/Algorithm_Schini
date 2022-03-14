import sys

blank_loc, sudoku_info = list(), list()
check_row, check_col, check_box = list(), list(), list()
for _ in range(9):
    sudoku_info.append([False] * 9)
    check_row.append([False] * 9)
    check_col.append([False] * 9)
    check_box.append([False] * 9)

input = sys.stdin.readline
for row in range(9):
    for col, num in enumerate(input().split()):
        sudoku_info[row][col] = num
        if num == '0':
            blank_loc.append((row, col))
        else:
            check_row[row][int(num) - 1] = True
            check_col[col][int(num) - 1] = True
            check_box[row // 3 * 3 + col // 3][int(num) - 1] = True
n = len(blank_loc)
escape = 0

def sudoku(depth: int):
    global escape
    if depth == n:
        escape = 1
        return
    row, col = blank_loc[depth]
    for i in range(9):
        if check_row[row][i] or check_col[col][i] or check_box[row // 3 * 3 + col // 3][i]:
            continue
        check_row[row][i] = True
        check_col[col][i] = True
        check_box[row // 3 * 3 + col // 3][i] = True
        sudoku_info[row][col] = str(i + 1)
        sudoku(depth + 1)
        if escape:
            return
        check_row[row][i] = False
        check_col[col][i] = False
        check_box[row // 3 * 3 + col // 3][i] = False

sudoku(0)
print('\n'.join([' '.join(row) for row in sudoku_info]))