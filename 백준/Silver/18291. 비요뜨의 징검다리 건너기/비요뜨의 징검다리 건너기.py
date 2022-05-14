import sys
input = sys.stdin.readline


def sol(n: int) -> str:
    a = 2; b = max(n-2, 0); ans = 1
    while b:
        a %= 1_000_000_007
        if b&1:
            ans = ans * a % 1_000_000_007
        a *= a
        b//=2
    return str(ans)


print('\n'.join(sol(int(input())) for _ in range(int(input()))))
