import sys
input = sys.stdin.readline


if __name__ == '__main__':
    a1, a0 = map(int, input().split())
    c, n0 = int(input()), int(input())
    if c < a1 or c*n0 < a1*n0 + a0:
        print(0)
    else:
        print(1)
 