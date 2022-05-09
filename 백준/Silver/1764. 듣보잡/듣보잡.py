import sys
input = sys.stdin.readline


def sol(n: int, m: int) -> str:
    both = list()
    add_both = both.append
    if n > m:
        never_heard = iter(input().rstrip() for _ in range(n))
        never_seen = {input().rstrip() for _ in range(m)}
        for name in never_heard:
            if name in never_seen:
                add_both(name)
    else:
        never_heard = {input().rstrip() for _ in range(n)}
        for _ in range(m):
            if (name := input().rstrip()) in never_heard:
                add_both(name)

    print(len(both))
    return '\n'.join(sorted(both))


print(sol(*map(int, input().split())))
