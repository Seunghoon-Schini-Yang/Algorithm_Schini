def print_stars(x):
    print(' ' * (N-x) + '*' * ((x<<1)^1))
    if x == N:
        return
    print_stars(x+1)
    print(' ' * (N-x) + '*' * ((x<<1)^1))


N = int(input())
N -= 1
print_stars(0)
