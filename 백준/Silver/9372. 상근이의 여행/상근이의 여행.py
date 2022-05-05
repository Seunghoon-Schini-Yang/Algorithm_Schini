import sys
input = sys.stdin.readline

def sol(n: int, m: int) -> str:
    for _ in range(m):
        input()
    return str(n-1)


print('\n'.join(sol(*map(int, input().split())) for _ in range(int(input()))))
