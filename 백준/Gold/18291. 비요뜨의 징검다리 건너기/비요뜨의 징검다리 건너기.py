import sys
input = sys.stdin.readline


def get_rem(n: int) -> str:
    a = 2
    b = max(n-2, 0)
    ans = 1
    dnmnt = 1_000_000_007
    while b:
        a %= dnmnt
        if b&1:
            ans = ans * a % dnmnt
        a *= a
        b >>= 1
    return str(ans)


if __name__ == '__main__':
    print('\n'.join(get_rem(int(input())) for _ in range(int(input()))))
