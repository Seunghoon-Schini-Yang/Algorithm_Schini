# dp
def sol(n: int) -> tuple:
    cc = c = 1
    for _ in range(n-2):
        c, cc = c+cc, c
    return c, n-2


print(*sol(int(input())))
