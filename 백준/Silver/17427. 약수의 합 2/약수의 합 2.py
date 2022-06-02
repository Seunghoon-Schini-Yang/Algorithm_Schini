def sol(n: int) -> int:
    return n**2 - sum(n%i for i in range(1, n+1))


print(sol(int(input())))
