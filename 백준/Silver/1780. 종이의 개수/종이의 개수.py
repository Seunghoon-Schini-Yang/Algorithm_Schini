from collections import defaultdict
import sys
input = sys.stdin.readline

def solution(n: int) -> None:
    digits = [input().split() for _ in range(n)]
    dg_cnt = defaultdict(int)

    result = divide_conquer(0, 0, n, digits, dg_cnt)

    for digit in ('-1', '0', '1'):
        if result == digit:
            dg_cnt[digit] += 1
        print(dg_cnt[digit])


def divide_conquer(v_s: int, h_s: int, dist: int, digits: list, dg_cnt: list) -> None:
    if dist == 1:
        return digits[v_s][h_s]
    
    digit_dict = defaultdict(int)
    dist //= 3

    for i in range(3):
        for j in range(3):
            digit = divide_conquer(v_s + i * dist, h_s + j * dist, dist, digits, dg_cnt)
            digit_dict[digit] += 1

    for digit in ('-1', '0', '1'):
        if digit_dict[digit] == 9:
            return digit
        dg_cnt[digit] += digit_dict[digit]

    return '-2'
    

solution(int(input()))
