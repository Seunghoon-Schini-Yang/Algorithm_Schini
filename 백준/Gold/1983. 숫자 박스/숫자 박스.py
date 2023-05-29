# https://schini.tistory.com/entry/%EC%88%AB%EC%9E%90-%EB%B0%95%EC%8A%A4-1983%EB%B2%88-%EB%B0%B1%EC%A4%80-BOJ
import sys
input = sys.stdin.readline


def check(i, r, c):
    maxy = 0
    if 0 <= i-r < erl and 0 <= i-c < ecl:
        maxy = memo[r][c] + row[i-r]*col[i-c]
        if 0 < r:
            maxy = max(maxy, memo[r-1][c])
        if 0 < c:
            maxy = max(maxy, memo[r][c-1])
        memo[r][c] = maxy


if __name__ == '__main__':
    N = int(input())
    row = [r for r in map(int, input().split()) if r]
    col = [c for c in map(int, input().split()) if c]
    rl = N-len(row)+1
    cl = N-len(col)+1
    erl, ecl = len(row), len(col)
    memo = [[0]*cl for _ in range(rl)]
    
    for i in range(N):
        for r in range(rl-1, -1, -1):
            for c in range(cl-1, -1, -1):
                check(i, r, c)
    print(max(max(row) for row in memo))
