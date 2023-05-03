import sys
input = sys.stdin.readline
from functools import reduce


def gcd(x, y):
    return y if not x%y else gcd(y, x%y)


if __name__ == '__main__':
    N = int(input())
    pos = int(input())
    steps = [-pos + (pos := int(input())) for _ in range(N-1)]
    _gcd = reduce(gcd, steps)
    print(sum( map( lambda x: x//_gcd - 1, steps ) ))
