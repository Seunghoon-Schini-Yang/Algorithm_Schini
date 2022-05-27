# dynamic programming
def sol(n: int) -> int:
    a,b,c = 2, 1, 1
    for _ in range(n-1):
        a, b, c = a*2+b+c, a+c, a+b
    return a


print(sol(int(input())))
