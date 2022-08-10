import sys
input = sys.stdin.readline


def is_inrange(r: int, c: int) -> bool:
    if r < N and c < N:
        return True
    return False


if __name__ == '__main__':
    N = int(input())
    house = [list(map(int, input().split())) for _ in range(N)]
    pipes = [[[0,0,0] for _ in range(N)] for _ in range(N)]
    pipes[0][1][0] = 1

    for r in range(N):
        for c in range(1, N):
            if house[r][c]:
                continue
            
            is_diag_poss = 0
            if is_inrange(r, c+1) and not house[r][c+1]:
                pipes[r][c+1][0] += pipes[r][c][0]+pipes[r][c][2]
                is_diag_poss += 1
            if is_inrange(r+1, c) and not house[r+1][c]:
                pipes[r+1][c][1] += pipes[r][c][1]+pipes[r][c][2]
                is_diag_poss += 1
            if is_inrange(r+1, c+1) and not house[r+1][c+1] and is_diag_poss == 2:
                pipes[r+1][c+1][2] += sum(pipes[r][c])

    print(sum(pipes[N-1][N-1]))
