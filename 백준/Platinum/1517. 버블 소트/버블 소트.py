# merge sort
import sys
input = sys.stdin.readline
cnt = 0


def sol(n: int) -> int:
    merge(n, list(map(int, input().split())))
    return cnt


def merge(n: int, arr: list) -> list:
    if n == 1:
        return arr
    
    global cnt
    f_len, b_len = n>>1, (n>>1)+(n&1)
    front = merge(f_len, arr[:n>>1])
    back = merge(b_len, arr[n>>1:])

    arr = [0]*n
    f_i = 0
    for b_i in range(b_len):
        while f_i < f_len and front[f_i] <= back[b_i]:
            arr[f_i+b_i] = front[f_i]
            f_i += 1
        arr[f_i+b_i] = back[b_i]
        cnt += f_len - f_i
        if f_i == f_len:
            break
    
    b_i += 1
    while b_i < b_len:
        arr[f_i+b_i] = back[b_i]
        b_i += 1

    while f_i < f_len:
        arr[f_i+b_i] = front[f_i]
        f_i += 1

    return arr


print(sol(int(input())))
