import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    colors = [input() for _ in range(n)]
    return divide_conquer(0, n, 0, n, colors)


def divide_conquer(v_s: int, v_e: int, h_s: int, h_e: int, colors: list) -> None:
    if v_e - v_s == 1:
        return colors[v_s][h_s]
    
    dist = (v_e - v_s) // 2

    one = divide_conquer(v_s, v_s + dist, h_s, h_s + dist, colors)
    two = divide_conquer(v_s, v_s + dist, h_s + dist, h_e, colors)
    three = divide_conquer(v_s + dist, v_e, h_s, h_s + dist, colors)
    four = divide_conquer(v_s + dist, v_e, h_s + dist, h_e, colors)

    if one == two == three == four == '0': return '0'
    if one == two == three == four == '1': return '1'

    return '(' + one + two + three + four + ')'
    

print(solution(int(input())))
