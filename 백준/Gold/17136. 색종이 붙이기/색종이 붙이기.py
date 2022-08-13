import sys
input = sys.stdin.readline


def backtrack(r: int, c: int) -> None:
    global miny

    if c == 10:
        backtrack(r+1, 0)
    elif r == 10:
        miny = min(miny, sum(attached))
    elif not paper[r][c]:
        c += 1
        while c < 10 and not paper[r][c]:
            c += 1
        backtrack(r, c)
    else:
        i = 1
        while i < 5:
            if r+i >= 10 or c+i >= 10 or not paper[r+i][c+i]:
                break
            is_break = False
            for j in range(i):
                if not paper[r+i][c+j] or not paper[r+j][c+i]:
                    is_break = True
                    break
            if is_break:
                break
            i += 1

        for j in range(i):
            paper[r+j][c+j] = 0
            for k in range(j):
                paper[r+j][c+k] = paper[r+k][c+j] = 0
        
        for j in range(i-1, -1, -1):
            if attached[j] < 5:
                attached[j] += 1
                backtrack(r, c+j)
                attached[j] -= 1

            paper[r+j][c+j] = 1
            for k in range(j):
                paper[r+j][c+k] = paper[r+k][c+j] = 1
    return


if __name__ == '__main__':
    miny = 26
    attached = [0]*5
    paper = [list(map(int, input().split())) for _ in range(10)]
    is_break = False
    backtrack(0, 0)
    print(miny if miny < 26 else -1)
