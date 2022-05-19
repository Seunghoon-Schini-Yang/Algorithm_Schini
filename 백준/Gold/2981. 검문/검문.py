import sys
input = sys.stdin.readline
from math import gcd, sqrt


def sol(n: int) -> list:
    x, y = int(input()), int(input())
    g = abs(x-y)
    x = y
    for _ in range(n-2):
        y = int(input())
        g = gcd(g, abs(x-y))
        x = y

    div_arr = [g]
    for i in range(2, int(sqrt(g))+1):
        quo, rem = divmod(g, i)
        if not rem:
            div_arr.append(i)
            if i != quo:
                div_arr.append(quo)
    
    return sorted(div_arr)


print(*sol(int(input())))
