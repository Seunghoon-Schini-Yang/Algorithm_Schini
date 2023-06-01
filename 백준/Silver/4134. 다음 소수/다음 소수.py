import sys
input = sys.stdin.readline


def sgp(n):
    n = max(n, 2)
    while True:
        for i in range(2, int(n**0.5)+1):
            if not n%i:
                break
        else:
            return str(n)
        n += 1


if __name__ == '__main__':
    print('\n'.join(sgp(int(input())) for _ in range(int(input()))))
