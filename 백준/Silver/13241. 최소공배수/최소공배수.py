def run_euclid(x, y):
    if not x%y:
        return y
    return run_euclid(y, x%y)


if __name__ == '__main__':
    x, y = map(int, input().split())
    gcd = run_euclid(x, y)
    print(x // gcd * y)