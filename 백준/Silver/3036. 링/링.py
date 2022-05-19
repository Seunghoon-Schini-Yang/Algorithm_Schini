import sys
print = sys.stdout.write


def sol() -> None:
    rings = map(int, input().split())
    div = next(rings)
    for r in rings:
        g = gcd(r, div)
        print(f'{div//g}/{r//g}\n')
    return


def gcd(a: int, b: int) -> int:
    if b:
        return gcd(b, a%b)
    return a


input()
sol()
