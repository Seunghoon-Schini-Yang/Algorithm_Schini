import sys
input = sys.stdin.readline
print = sys.stdout.write


def sol(n: int) -> None:
    for _ in range(n):
        a,b = map(int, input().split())
        if a > b:
            a,b = b,a
        print(f'{a*b//gcd(a,b)}\n')


def gcd(a: int, b: int) -> int:
    if not a:
        return b
    return gcd(b%a, a)


sol(int(input()))
