import sys
input = sys.stdin.readline


def main(N: int):
    memo = [[0] * 101 for _ in range(101)]
    for _ in range(N):
        x, y = map(int, input().split())
        memo[x][y] += 1
        memo[x][y+10] -= 1
        memo[x+10][y] -= 1
        memo[x+10][y+10] += 1

    for r in range(100):
        for c in range(100):
            memo[r][c+1] += memo[r][c]
    for c in range(100):
        for r in range(100):
            memo[r+1][c] += memo[r][c]
    return sum(sum(1 if x else 0 for x in row[:-1]) for row in memo[:-1])


if __name__ == '__main__':
    area = main(int(input()))
    print(area)
