import sys


def main():
    for line in sys.stdin.readlines()[:-1]:
        a, b, c = sorted(map(int, line.split()))
        if a + b <= c:
            print('Invalid')
        elif a == b == c:
            print('Equilateral')
        elif a == b or b == c or c == a:
            print('Isosceles')
        else:
            print('Scalene')


if __name__ == '__main__':
    main()
