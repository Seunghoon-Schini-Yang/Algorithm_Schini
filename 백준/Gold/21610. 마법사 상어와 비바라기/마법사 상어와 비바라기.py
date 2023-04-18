import sys
input = sys.stdin.readline


def main():
    clouds = {(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)}
    for _ in range(M):
        d, s = map(int, input().split())
        # 1
        clouds = {move_cloud(r, c, d, s) for r, c in clouds}
        # 2
        for r, c in clouds:
            A[r][c] += 1
        # 3
        # 4
        for r, c in clouds:
            A[r][c] += copy_diags(r, c)
        # 5
        tmp = set()
        for r in range(N):
            for c in range(N):
                if 2 <= A[r][c] and (r, c) not in clouds:
                    A[r][c] -= 2
                    tmp.add((r, c))
        clouds = tmp
    
    return sum(sum(row) for row in A)
    


def move_cloud(r, c, d, s):
    return ((r + (move_cloud_r[d] * s)) % N, (c + (move_cloud_c[d] * s)) % N)


def copy_diags(r, c):
    cnt = 0
    if 0 < r:
        if 0 < c:
            if A[r-1][c-1]:  cnt += 1
        if c < N-1:
            if A[r-1][c+1]:  cnt += 1
    if r < N-1:
        if 0 < c:
            if A[r+1][c-1]:  cnt += 1
        if c < N-1:
            if A[r+1][c+1]:  cnt += 1
    return cnt


if __name__ == '__main__':
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    move_cloud_r = (0, 0, -1, -1, -1, 0, 1, 1, 1)
    move_cloud_c = (0, -1, -1, 0, 1, 1, 1, 0, -1)
    water_all = main()
    print(water_all)
