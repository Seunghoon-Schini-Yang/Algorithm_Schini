import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    colors = [list(map(int, input().split())) for _ in range(n)]
    wb_cnt = [0, 0]

    result = divide_conquer(0, n, 0, n, colors, wb_cnt)

    if result == 0:
        wb_cnt = [1, 0]
    elif result == 1:
        wb_cnt = [0, 1]

    print(wb_cnt[0])
    print(wb_cnt[1])


def divide_conquer(v_s: int, v_e: int, h_s: int, h_e: int, colors: list, wb_cnt: list) -> None:
    if v_e - v_s == 1:
        return colors[v_s][h_s]
    
    dist = (v_e - v_s) // 2

    one = divide_conquer(v_s, v_s + dist, h_s, h_s + dist, colors, wb_cnt)
    two = divide_conquer(v_s + dist, v_e, h_s, h_s + dist, colors, wb_cnt)
    three = divide_conquer(v_s, v_s + dist, h_s + dist, h_e, colors, wb_cnt)
    four = divide_conquer(v_s + dist, v_e, h_s + dist, h_e, colors, wb_cnt)

    if one == two == three == four == 0: return 0
    if one == two == three == four == 1: return 1

    for block in (one, two, three, four):
        if block == 1:
            wb_cnt[1] += 1
        elif block == 0:
            wb_cnt[0] += 1

    return -1
    

solution(int(input()))
