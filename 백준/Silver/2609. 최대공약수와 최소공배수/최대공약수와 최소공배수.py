def sol(a: int, b: int) -> str:
    if a > b:
        a,b = b,a
    g = gcd(a,b)
    return f'{g}\n{a*b//g}'


def gcd(a: int, b: int) -> int:
    if not b%a:
        return a
    return gcd(b%a, a)


print(sol(*map(int, input().split())))