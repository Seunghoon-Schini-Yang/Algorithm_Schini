import sys
input = sys.stdin.readline


if __name__ == '__main__':
    input()
    mod = 1_000_000_007
    w = h = e1 = e2 = 0
    for char in input().rstrip():
        if char == 'W':
            w += 1
        elif char == 'H':
            h += w
        elif char == 'E':
            e2 = (e2*2 + e1) % mod
            e1 = (e1+h) % mod
    print(e2)