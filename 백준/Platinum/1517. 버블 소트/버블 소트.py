# merge sort
cnt = 0


def sol(n: int) -> int:
    merge(n, list(map(int, input().split())))
    return cnt


def merge(n: int, arr: list) -> list:
    if n == 1:
        return arr
    
    global cnt
    front = merge(n>>1, arr[:n>>1])
    back = merge((n>>1)+(n&1), arr[n>>1:])

    arr = [0]*n
    f_i = 0
    for b_i in range((n>>1)+(n&1)):
        while f_i < n>>1 and front[f_i] <= back[b_i]:
            arr[f_i+b_i] = front[f_i]
            f_i += 1
        arr[f_i+b_i] = back[b_i]
        cnt += (n>>1) - f_i
        if f_i == n>>1:
            break
    
    b_i += 1
    while b_i < (n>>1)+(n&1):
        arr[f_i+b_i] = back[b_i]
        b_i += 1

    while f_i < n>>1:
        arr[f_i+b_i] = front[f_i]
        f_i += 1

    return arr


print(sol(int(input())))
