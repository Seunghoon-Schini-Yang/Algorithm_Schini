import sys
input = sys.stdin.readline


def sol(m: int, n: int) -> int:
    cnt = 0
    flag = False
    unis = [list(map(int, input().split())) for _ in range(m)]
    for i in range(1, m):
        for j in range(i):
            flag = False
            for x in range(1, n):
                for y in range(x):
                    i_diff = unis[i][x] - unis[i][y]
                    j_diff = unis[j][x] - unis[j][y]
                    if i_diff == j_diff == 0:
                        continue
                    if i_diff * j_diff <= 0:
                        flag = True
                        break
                if flag:
                    break
            if flag:
                continue
            cnt += 1
    return cnt


print(sol(*map(int, input().split())))
