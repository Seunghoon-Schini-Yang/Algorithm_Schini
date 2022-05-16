import math


def sol(a: int, b: int) -> str:
    if a > b:
        a,b = b,a
    g = math.gcd(a,b)
    return f'{g}\n{a*b//g}'


'''
def gcd(a: int, b: int) -> int:
    if not b%a:
        return a
    return gcd(a, b%a)
'''

print(sol(*map(int, input().split())))
