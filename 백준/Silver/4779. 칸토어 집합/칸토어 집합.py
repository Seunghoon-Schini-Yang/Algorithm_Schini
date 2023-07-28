import sys


def rec(x):
    if x == 0:
        return '-'
    return rec(x-1) + ' ' * pow(3, x-1) + rec(x-1)


if __name__ == '__main__':
    print('\n'.join(rec(int(x)) for x in sys.stdin.readlines()))
