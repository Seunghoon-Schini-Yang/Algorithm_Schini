# https://developer-ellen.tistory.com/54 코드 참고
# backtracking + dfs (recursive)
import sys
input = sys.stdin.readline


def sol() -> int:
    dfs(0, -1)
    return miny if miny < 4 else -1


def check() -> bool:
    for col in range(1, n):
        cc = col
        for row in range(1, h+1):
            if ladder[row][cc-1]:
                cc -= 1
            elif ladder[row][cc]:
                cc += 1
        if cc != col:
            return False
    return True


def dfs(depth: int, idx: int) -> None:
    global miny
    
    if depth >= miny:
        return
    if check():
        miny = depth
        return
    
    for i in range(idx+1, avail_len):
        row = avail[i][0]; col = avail[i][1]
        if not ladder[row][col-1]:
            ladder[row][col] = 1
            dfs(depth+1, i)
            ladder[row][col] = 0
    return


if __name__ == '__main__':
    miny = 4
    n,m,h = map(int, input().split())
    
    ladder = [[0]*(n+1) for _ in range(h+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        ladder[a][b] = 1
    
    avail = [(r,c) for c in range(1, n) for r in range(1, h+1) if not ladder[r][c-1] and not ladder[r][c] and not ladder[r][c+1]]
    avail_len = len(avail)
    print(sol())
