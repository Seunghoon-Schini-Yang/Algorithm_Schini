def sol(n: int) -> int:
    k = 5; cnt = 0
    while n//k:
        cnt += n//k
        k *= 5
    return cnt


print(sol(int(input())))
