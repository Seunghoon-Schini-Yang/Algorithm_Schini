import sys
input_ = sys.stdin.read


def sol(n: int, m: int) -> None:
    I = input_().splitlines()
    never_heard = set(I[:n])
    never_seen = set(I[n:])

    both = sorted(never_heard.intersection(never_seen))

    print(len(both))
    for name in both:
        print(name)


sol(*map(int, input().split()))
