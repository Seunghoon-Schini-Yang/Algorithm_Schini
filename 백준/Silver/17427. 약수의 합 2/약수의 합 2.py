def sol(n: int) -> int:
    return sum(i * (n//i) for i in range(1, n+1))


print(sol(int(input())))
